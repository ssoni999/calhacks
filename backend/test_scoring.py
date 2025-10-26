#!/usr/bin/env python3
"""
Quick test script to see AI scoring in action
"""
from database import SessionLocal
import models
from ai_scorer import score_candidate_with_ai, load_job_description, load_rubric

def test_single_candidate():
    """Test scoring a single candidate and display results"""
    db = SessionLocal()
    
    # Get first Software Engineer candidate
    candidate = db.query(models.Candidate).filter(
        models.Candidate.position == "Software Engineer"
    ).first()
    
    if not candidate:
        print("❌ No Software Engineer candidates found. Run init_db.py first.")
        return
    
    print("🎯 Testing AI Scoring")
    print("=" * 60)
    print(f"Candidate: {candidate.name}")
    print(f"Position: {candidate.position}")
    print(f"Email: {candidate.email}")
    print("=" * 60)
    
    # Load job description and rubric
    print("\n📄 Loading job description and rubric...")
    job_desc = load_job_description(candidate.position)
    rubric = load_rubric(candidate.position)
    
    print(f"✅ Loaded {len(job_desc)} chars of job description")
    print(f"✅ Loaded {len(rubric)} chars of rubric")
    
    # Score the candidate
    print(f"\n🤖 Scoring {candidate.name} with Claude AI...")
    print("(This will take 5-10 seconds...)")
    
    result = score_candidate_with_ai(candidate.id, job_desc, rubric)
    
    # Display results
    print("\n" + "=" * 60)
    print("📊 RESULTS")
    print("=" * 60)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return
    
    scores = result["scores"]
    print(f"\n✨ {result['candidate_name']}")
    print(f"   Experience Score:    {scores['experience_score']}/100")
    print(f"   Skills Score:        {scores['skills_score']}/100")
    print(f"   Education Score:     {scores['education_score']}/100")
    print(f"   Cultural Fit Score:  {scores['cultural_fit_score']}/100")
    print(f"   Overall Score:       {scores['overall_score']}/100")
    
    print(f"\n💪 Strengths: {scores['strengths']}")
    print(f"⚠️  Weaknesses: {scores['weaknesses']}")
    print(f"🎯 Recommendation: {scores['recommendation'].upper()}")
    
    print("\n" + "=" * 60)
    print("✅ Score saved to database!")
    print("   View in frontend or run: python view_scores.py")
    
    db.close()

if __name__ == "__main__":
    test_single_candidate()
