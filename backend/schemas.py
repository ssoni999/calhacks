from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class RecruiterBase(BaseModel):
    name: str
    email: str

class RecruiterCreate(RecruiterBase):
    pass

class Recruiter(RecruiterBase):
    id: int
    
    class Config:
        from_attributes = True

class CandidateBase(BaseModel):
    name: str
    email: str
    position: str
    resume_text: str

class CandidateCreate(CandidateBase):
    recruiter_id: int

class CandidateUpdate(BaseModel):
    stage: Optional[str] = None
    notes: Optional[str] = None
    is_rejected: Optional[bool] = None

class Candidate(CandidateBase):
    id: int
    stage: str
    notes: str
    experience_score: Optional[float] = None
    skills_score: Optional[float] = None
    education_score: Optional[float] = None
    overall_score: Optional[float] = None
    cultural_fit_score: Optional[float] = None
    analysis_notes: str
    recruiter_id: int
    is_rejected: bool = False
    
    class Config:
        from_attributes = True

