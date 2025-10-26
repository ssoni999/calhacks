import os
import json
import requests
import time
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

LAVA_TOKEN = os.getenv("LAVA_FORWARD_TOKEN")
LAVA_BASE_URL = os.getenv("LAVA_BASE_URL")
CLAUDE_HAIKU = "claude-3-haiku-20240307"

# Get project root directory
PROJECT_ROOT = Path(__file__).parent.parent
JOB_DESC_DIR = PROJECT_ROOT / "job_descriptions"
RUBRIC_DIR = PROJECT_ROOT / "rubrics"

def load_job_description(position: str) -> str:
    """Load job description from file based on position"""
    position_map = {
        "Software Engineer": "software_engineer.md",
        "Senior Software Engineer": "senior_software_engineer.md",
        "Frontend Engineer": "frontend_engineer.md",
        "DevOps Engineer": "devops_engineer.md",
        "Data Engineer": "data_engineer.md",
        "Backend Engineer": "backend_engineer.md",
        "Full Stack Developer": "full_stack_developer.md"
    }
    
    filename = position_map.get(position)
    if not filename:
        raise ValueError(f"No job description found for position: {position}")
    
    filepath = JOB_DESC_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Job description file not found: {filepath}")
    
    return filepath.read_text()

def load_rubric(position: str) -> str:
    """Load rubric from file based on position"""
    position_map = {
        "Software Engineer": "software_engineer_rubric.md",
        "Senior Software Engineer": "senior_software_engineer_rubric.md",
        "Frontend Engineer": "frontend_engineer_rubric.md",
        "DevOps Engineer": "devops_engineer_rubric.md",
        "Data Engineer": "data_engineer_rubric.md",
        "Backend Engineer": "backend_engineer_rubric.md",
        "Full Stack Developer": "full_stack_developer_rubric.md"
    }
    
    filename = position_map.get(position)
    if not filename:
        raise ValueError(f"No rubric found for position: {position}")
    
    filepath = RUBRIC_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Rubric file not found: {filepath}")
    
    return filepath.read_text()

def score_candidate_with_ai(candidate_id: int, job_description: str, rubric: str):
    """Score a single candidate using Claude AI via Lava"""
    db = SessionLocal()
    try:
        candidate = db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()
        if not candidate:
            return {"error": "Candidate not found"}
        
        # Build prompt
        prompt = f"""You are an expert technical recruiter. Evaluate this candidate's resume against the job requirements.

JOB DESCRIPTION:
{job_description}

EVALUATION RUBRIC:
{rubric}

CANDIDATE RESUME:
{candidate.resume_text}

Provide a structured evaluation with scores (0-100) for each criterion. Return ONLY valid JSON in this exact format:
{{
  "experience_score": <number>,
  "skills_score": <number>,
  "education_score": <number>,
  "cultural_fit_score": <number>,
  "overall_score": <number>,
  "strengths": "<brief summary>",
  "weaknesses": "<brief summary>",
  "recommendation": "<hire/maybe/pass>"
}}"""

        # Call Claude via Lava
        url = f"{LAVA_BASE_URL}/forward?u=https://api.anthropic.com/v1/messages"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LAVA_TOKEN}",
            "anthropic-version": "2023-06-01"
        }
        body = {
            "model": CLAUDE_HAIKU,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        # Retry logic for API calls
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(url, headers=headers, json=body, timeout=30)
                response.raise_for_status()
                break
            except requests.exceptions.RequestException as e:
                if attempt == max_retries - 1:
                    print(f"⚠️  API failed after {max_retries} attempts. Using fallback scoring.")
                    # Fallback: assign default scores
                    scores = {
                        "experience_score": 50,
                        "skills_score": 50,
                        "education_score": 50,
                        "cultural_fit_score": 50,
                        "overall_score": 50,
                        "strengths": "API unavailable - manual review needed",
                        "weaknesses": "API unavailable - manual review needed",
                        "recommendation": "maybe"
                    }
                    # Update candidate in database
                    candidate.experience_score = scores["experience_score"]
                    candidate.skills_score = scores["skills_score"]
                    candidate.education_score = scores["education_score"]
                    candidate.overall_score = scores["overall_score"]
                    candidate.analysis_notes = "API unavailable - requires manual review"
                    db.commit()
                    db.refresh(candidate)
                    return {
                        "candidate_id": candidate_id,
                        "candidate_name": candidate.name,
                        "scores": scores,
                        "status": "fallback"
                    }
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {2 ** attempt} seconds...")
                time.sleep(2 ** attempt)
        
        # Parse response (only if we got here successfully)
        result = response.json()
        print(f"API Response: {result}")
        
        content = result["content"][0]["text"]
        print(f"Raw content: {content}")
        
        # Check if Claude refused to score (insufficient resume)
        if "do not have enough details" in content.lower() or "unable to provide" in content.lower():
            print("⚠️  Resume insufficient for AI scoring. Using default low scores.")
            scores = {
                "experience_score": 20,
                "skills_score": 20,
                "education_score": 20,
                "cultural_fit_score": 20,
                "overall_score": 20,
                "strengths": "N/A - Insufficient resume data",
                "weaknesses": "Resume lacks detail about experience, skills, and qualifications",
                "recommendation": "pass"
            }
        else:
            # Extract JSON from content (handle markdown code blocks)
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            scores = json.loads(content)
        
        # Update candidate in database
        candidate.experience_score = scores["experience_score"]
        candidate.skills_score = scores["skills_score"]
        candidate.education_score = scores["education_score"]
        candidate.overall_score = scores["overall_score"]
        candidate.analysis_notes = f"AI Evaluation - Strengths: {scores['strengths']} | Weaknesses: {scores['weaknesses']} | Recommendation: {scores['recommendation']}"
        
        db.commit()
        db.refresh(candidate)
        
        return {
            "candidate_id": candidate_id,
            "candidate_name": candidate.name,
            "scores": scores,
            "status": "success"
        }
        
    except Exception as e:
        db.rollback()
        return {"error": str(e), "candidate_id": candidate_id}
    finally:
        db.close()

def score_all_candidates_for_position(position: str, job_description: str = None, rubric: str = None):
    """Score all candidates for a specific position
    
    If job_description and rubric are not provided, they will be loaded from files.
    """
    db = SessionLocal()
    try:
        # Load from files if not provided
        if job_description is None:
            job_description = load_job_description(position)
        if rubric is None:
            rubric = load_rubric(position)
        
        candidates = db.query(models.Candidate).filter(models.Candidate.position == position).all()
        results = []
        
        for candidate in candidates:
            print(f"Scoring {candidate.name}...")
            result = score_candidate_with_ai(candidate.id, job_description, rubric)
            results.append(result)
        
        return {
            "position": position,
            "total_candidates": len(candidates),
            "results": results
        }
    finally:
        db.close()

def score_all_candidates_auto():
    """Score all candidates automatically using their position's job description and rubric"""
    db = SessionLocal()
    try:
        # Get all unique positions
        positions = db.query(models.Candidate.position).distinct().all()
        all_results = []
        
        for (position,) in positions:
            print(f"\n{'='*60}")
            print(f"Scoring candidates for position: {position}")
            print(f"{'='*60}")
            
            try:
                result = score_all_candidates_for_position(position)
                all_results.append(result)
            except (ValueError, FileNotFoundError) as e:
                print(f"⚠️  Skipping {position}: {e}")
                continue
        
        return {
            "total_positions": len(all_results),
            "positions": all_results
        }
    finally:
        db.close()

if __name__ == "__main__":
    # Score all candidates automatically using their position's files
    results = score_all_candidates_auto()
    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    print(json.dumps(results, indent=2))
