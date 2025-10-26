#!/usr/bin/env python3
"""
View all candidate scores from the database
"""
from database import SessionLocal
import models

def view_all_scores():
    """Display all candidate scores in a nice format"""
    db = SessionLocal()
    
    candidates = db.query(models.Candidate).all()
    
    print("\n" + "=" * 80)
    print("📊 CANDIDATE SCORES DATABASE")
    print("=" * 80)
    
    if not candidates:
        print("❌ No candidates found. Run init_db.py first.")
        return
    
    for i, c in enumerate(candidates, 1):
        print(f"\n{i}. {c.name} - {c.position}")
        print(f"   Email: {c.email}")
        print(f"   Stage: {c.stage}")
        
        if c.overall_score:
            print(f"\n   📈 Scores:")
            print(f"      Experience:   {c.experience_score or 'N/A'}/100")
            print(f"      Skills:       {c.skills_score or 'N/A'}/100")
            print(f"      Education:    {c.education_score or 'N/A'}/100")
            print(f"      Cultural Fit: {c.cultural_fit_score or 'N/A'}/100")
            print(f"      Overall:      {c.overall_score}/100")
            
            if c.analysis_notes:
                print(f"\n   💡 AI Analysis:")
                print(f"      {c.analysis_notes}")
        else:
            print(f"   ⏳ Not yet scored by AI")
        
        print("   " + "-" * 76)
    
    # Summary
    scored = [c for c in candidates if c.overall_score]
    print(f"\n📊 Summary: {len(scored)}/{len(candidates)} candidates scored")
    
    if scored:
        avg_overall = sum(c.overall_score for c in scored) / len(scored)
        print(f"📈 Average Overall Score: {avg_overall:.1f}/100")
    
    print("=" * 80 + "\n")
    
    db.close()

if __name__ == "__main__":
    view_all_scores()
