from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import os

from database import SessionLocal, engine, Base
import models
import schemas
from ai_scorer import score_candidate_with_ai, score_all_candidates_for_position

# Set datetime for models
from sqlalchemy import event
from sqlalchemy.orm import Session as SQLSession

@event.listens_for(models.Recruiter, 'before_insert')
def set_recruiter_created_at(mapper, connection, target):
    target.created_at = datetime.now()

@event.listens_for(models.Candidate, 'before_insert')
def set_candidate_created_at(mapper, connection, target):
    target.created_at = datetime.now()

app = FastAPI(title="RecruitAI - Streamlined Hiring Platform")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize database
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "RecruitAI API is running"}

# Recruiter endpoints
@app.post("/api/recruiters", response_model=schemas.Recruiter)
def create_recruiter(recruiter: schemas.RecruiterCreate, db: Session = Depends(get_db)):
    db_recruiter = models.Recruiter(name=recruiter.name, email=recruiter.email)
    db.add(db_recruiter)
    db.commit()
    db.refresh(db_recruiter)
    return db_recruiter

@app.get("/api/recruiters", response_model=List[schemas.Recruiter])
def get_recruiters(db: Session = Depends(get_db)):
    return db.query(models.Recruiter).all()

@app.get("/api/recruiters/{recruiter_id}", response_model=schemas.Recruiter)
def get_recruiter(recruiter_id: int, db: Session = Depends(get_db)):
    recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == recruiter_id).first()
    if not recruiter:
        raise HTTPException(status_code=404, detail="Recruiter not found")
    return recruiter

# Candidate endpoints
@app.post("/api/candidates", response_model=schemas.Candidate)
def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    # AI-powered resume analysis
    analysis = analyze_resume(candidate.resume_text, candidate.position)
    
    db_candidate = models.Candidate(
        name=candidate.name,
        email=candidate.email,
        position=candidate.position,
        resume_text=candidate.resume_text,
        stage="Resume Review",
        recruiter_id=candidate.recruiter_id,
        experience_score=analysis.get("experience_score", 0),
        skills_score=analysis.get("skills_score", 0),
        education_score=analysis.get("education_score", 0),
        overall_score=analysis.get("overall_score", 0),
        analysis_notes=analysis.get("notes", "")
    )
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

@app.get("/api/candidates", response_model=List[schemas.Candidate])
def get_candidates(
    recruiter_id: Optional[int] = None,
    stage: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Candidate)
    if recruiter_id:
        query = query.filter(models.Candidate.recruiter_id == recruiter_id)
    if stage:
        query = query.filter(models.Candidate.stage == stage)
    return query.all()

@app.put("/api/candidates/{candidate_id}", response_model=schemas.Candidate)
def update_candidate(
    candidate_id: int,
    candidate: schemas.CandidateUpdate,
    db: Session = Depends(get_db)
):
    db_candidate = db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()
    if not db_candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    
    if candidate.stage:
        db_candidate.stage = candidate.stage
    if candidate.notes:
        db_candidate.notes = candidate.notes
    
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

# KPI endpoints
@app.get("/api/recruiters/{recruiter_id}/kpis")
def get_recruiter_kpis(recruiter_id: int, db: Session = Depends(get_db)):
    candidates = db.query(models.Candidate).filter(models.Candidate.recruiter_id == recruiter_id).all()
    
    total_candidates = len(candidates)
    resume_review = len([c for c in candidates if c.stage == "Resume Review"])
    phone_screen = len([c for c in candidates if c.stage == "Phone Screen"])
    technical_interview = len([c for c in candidates if c.stage == "Technical Interview"])
    final_round = len([c for c in candidates if c.stage == "Final Round"])
    offers = len([c for c in candidates if c.stage == "Offer"])
    
    # Filter out None values for score calculations
    exp_scores = [c.experience_score for c in candidates if c.experience_score is not None]
    skill_scores = [c.skills_score for c in candidates if c.skills_score is not None]
    overall_scores = [c.overall_score for c in candidates if c.overall_score is not None]
    
    avg_experience_score = sum(exp_scores) / len(exp_scores) if exp_scores else 0
    avg_skills_score = sum(skill_scores) / len(skill_scores) if skill_scores else 0
    avg_overall_score = sum(overall_scores) / len(overall_scores) if overall_scores else 0
    
    return {
        "recruiter_id": recruiter_id,
        "total_candidates": total_candidates,
        "pipeline_breakdown": {
            "resume_review": resume_review,
            "phone_screen": phone_screen,
            "technical_interview": technical_interview,
            "final_round": final_round,
            "offers": offers
        },
        "average_scores": {
            "experience": round(avg_experience_score, 2),
            "skills": round(avg_skills_score, 2),
            "overall": round(avg_overall_score, 2)
        },
        "conversion_rate": round((offers / total_candidates * 100) if total_candidates > 0 else 0, 2)
    }

@app.get("/api/candidates/top-10")
def get_top_10_candidates(
    recruiter_id: Optional[int] = None,
    metric: str = "overall",
    db: Session = Depends(get_db)
):
    query = db.query(models.Candidate)
    if recruiter_id:
        query = query.filter(models.Candidate.recruiter_id == recruiter_id)
    
    # Order by selected metric, handling null values
    if metric == "overall":
        candidates = query.filter(models.Candidate.overall_score.isnot(None)).order_by(
            models.Candidate.overall_score.desc()
        ).limit(10).all()
    elif metric == "experience":
        candidates = query.filter(models.Candidate.experience_score.isnot(None)).order_by(
            models.Candidate.experience_score.desc()
        ).limit(10).all()
    else:
        candidates = query.filter(models.Candidate.skills_score.isnot(None)).order_by(
            models.Candidate.skills_score.desc()
        ).limit(10).all()
    
    return [schemas.Candidate.model_validate(c) for c in candidates]

def analyze_resume(resume_text: str, position: str) -> dict:
    """AI-powered resume analysis"""
    # Simulate AI analysis based on keywords and content
    experience_keywords = ["experience", "years", "worked", "developed", "implemented", "managed"]
    skills_keywords = ["python", "javascript", "react", "sql", "api", "backend", "frontend", "cloud"]
    education_keywords = ["university", "degree", "bachelor", "master", "phd", "graduated"]
    
    text_lower = resume_text.lower()
    
    experience_score = min(100, len([kw for kw in experience_keywords if kw in text_lower]) * 10)
    skills_score = min(100, len([kw for kw in skills_keywords if kw in text_lower]) * 15)
    education_score = min(100, len([kw for kw in education_keywords if kw in text_lower]) * 20)
    
    overall_score = (experience_score * 0.4 + skills_score * 0.4 + education_score * 0.2)
    
    notes = f"Analyzed for {position} position. Experience score based on relevant work history keywords."
    
    return {
        "experience_score": round(experience_score),
        "skills_score": round(skills_score),
        "education_score": round(education_score),
        "overall_score": round(overall_score),
        "notes": notes
    }

# AI Scoring endpoints
class AIScoreRequest(BaseModel):
    candidate_id: int
    job_description: str
    rubric: str

class AIScoreBatchRequest(BaseModel):
    position: str
    job_description: str
    rubric: str

@app.post("/api/ai/score-candidate")
def ai_score_candidate(request: AIScoreRequest):
    """Score a single candidate using AI"""
    result = score_candidate_with_ai(request.candidate_id, request.job_description, request.rubric)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/api/ai/score-position")
def ai_score_position(request: AIScoreBatchRequest):
    """Score all candidates for a position using AI"""
    result = score_all_candidates_for_position(request.position, request.job_description, request.rubric)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

