#!/usr/bin/env python3
import sys
from ai_scorer import score_candidate_with_ai, load_job_description, load_rubric
from database import SessionLocal
import models

if len(sys.argv) < 2:
    print("Usage: python score_single.py <candidate_email>")
    sys.exit(1)

candidate_email = sys.argv[1]

# Get candidate by email
db = SessionLocal()
candidate = db.query(models.Candidate).filter(models.Candidate.email == candidate_email).first()
db.close()

if not candidate:
    print(f"Candidate with email {candidate_email} not found")
    sys.exit(1)

print(f"Scoring candidate: {candidate.name} ({candidate.position})")
job_desc = load_job_description(candidate.position)
rubric = load_rubric(candidate.position)
result = score_candidate_with_ai(candidate.id, job_desc, rubric)
print(result)
