#!/usr/bin/env python3
"""
Script to calculate scores for all existing candidates in the database.
This is useful if the database already has candidates without scores.
"""

from sqlalchemy.orm import Session
from database import SessionLocal
import models

def analyze_resume(resume_text: str, position: str) -> dict:
    """AI-powered resume analysis based on keywords"""
    experience_keywords = ["experience", "years", "worked", "developed", "implemented", "managed", "led", "built", "created", "designed", "architected"]
    skills_keywords = ["python", "javascript", "react", "sql", "api", "backend", "frontend", "cloud", "docker", "kubernetes", "aws", "node", "django", "flask", "typescript", "java", "go", "terraform", "spark", "kafka"]
    education_keywords = ["university", "degree", "bachelor", "master", "phd", "graduated", "college", "gpa", "summa", "magna", "cum laude"]
    
    if not resume_text:
        return {
            "experience_score": 0,
            "skills_score": 0,
            "education_score": 0,
            "overall_score": 0,
            "notes": "No resume text provided"
        }
    
    text_lower = resume_text.lower()
    
    experience_score = min(100, len([kw for kw in experience_keywords if kw in text_lower]) * 8)
    skills_score = min(100, len([kw for kw in skills_keywords if kw in text_lower]) * 6)
    education_score = min(100, len([kw for kw in education_keywords if kw in text_lower]) * 15)
    
    # Ensure minimum scores based on resume length
    if len(resume_text) > 500:
        experience_score = max(experience_score, 30)
        skills_score = max(skills_score, 30)
        education_score = max(education_score, 30)
    
    overall_score = round(experience_score * 0.4 + skills_score * 0.4 + education_score * 0.2)
    
    notes = f"Analyzed for {position} position. Experience score based on relevant work history keywords, skills score based on technical keywords, education score based on academic credentials."
    
    return {
        "experience_score": round(experience_score),
        "skills_score": round(skills_score),
        "education_score": round(education_score),
        "overall_score": overall_score,
        "notes": notes
    }

def calculate_all_scores():
    """Calculate scores for all candidates in the database"""
    db: Session = SessionLocal()
    try:
        candidates = db.query(models.Candidate).all()
        print(f"Found {len(candidates)} candidates to score...")
        
        updated_count = 0
        for candidate in candidates:
            if not candidate.resume_text or not candidate.position:
                print(f"Skipping {candidate.name} - missing resume text or position")
                continue
            
            # Calculate scores
            analysis = analyze_resume(candidate.resume_text, candidate.position)
            
            # Update candidate scores
            candidate.experience_score = analysis["experience_score"]
            candidate.skills_score = analysis["skills_score"]
            candidate.education_score = analysis["education_score"]
            candidate.overall_score = analysis["overall_score"]
            candidate.analysis_notes = analysis["notes"]
            
            updated_count += 1
            print(f"Updated scores for {candidate.name} ({candidate.position}): Overall={analysis['overall_score']}, Experience={analysis['experience_score']}, Skills={analysis['skills_score']}, Education={analysis['education_score']}")
        
        db.commit()
        print(f"\n✅ Successfully updated scores for {updated_count} candidates!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    calculate_all_scores()

