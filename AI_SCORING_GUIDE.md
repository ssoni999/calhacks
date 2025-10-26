# AI Resume Scoring Guide

## Overview

The AI scoring system uses **Claude 3 Haiku** (cheapest Claude model) via Lava API to evaluate candidates against job-specific rubrics.

## Setup

1. **Add your Lava token** to `backend/.env`:
```bash
LAVA_FORWARD_TOKEN=your_token_here
LAVA_BASE_URL=https://api.lavapayments.com/v1
```

2. **Install dependencies**:
```bash
cd backend
pip install -r requirements.txt
```

## How It Works

### Automatic File Loading

The system automatically loads job descriptions and rubrics from:
- `job_descriptions/` - Job requirements and descriptions
- `rubrics/` - Evaluation criteria and scoring guidelines

### Supported Positions

- Software Engineer
- Senior Software Engineer
- Frontend Engineer
- DevOps Engineer
- Data Engineer

## Usage

### Option 1: Score All Candidates (Recommended)

```bash
cd backend
python run_ai_scoring.py
```

This will:
- Load job descriptions and rubrics for each position
- Score all candidates based on their position
- Save scores to database

### Option 2: Score Specific Position

```python
from ai_scorer import score_all_candidates_for_position

# Automatically loads from files
results = score_all_candidates_for_position("Software Engineer")
```

### Option 3: Use Custom Job Description/Rubric

```python
from ai_scorer import score_all_candidates_for_position

custom_job = "Your custom job description..."
custom_rubric = "Your custom rubric..."

results = score_all_candidates_for_position(
    "Software Engineer",
    job_description=custom_job,
    rubric=custom_rubric
)
```

### Option 4: Score Single Candidate

```python
from ai_scorer import score_candidate_with_ai

result = score_candidate_with_ai(
    candidate_id=1,
    job_description="Job description...",
    rubric="Evaluation rubric..."
)
```

## API Endpoints

### Score Single Candidate
```bash
POST /api/ai/score-candidate
{
  "candidate_id": 1,
  "job_description": "...",
  "rubric": "..."
}
```

### Score All Candidates for Position
```bash
POST /api/ai/score-position
{
  "position": "Software Engineer",
  "job_description": "...",
  "rubric": "..."
}
```

## Scores Generated

The AI evaluates each candidate on:

1. **Experience Score (0-100)**: Years of work, leadership, impact
2. **Skills Score (0-100)**: Technical proficiency in required technologies
3. **Education Score (0-100)**: Degree level, institution, coursework
4. **Cultural Fit Score (0-100)**: Communication, teamwork, growth mindset
5. **Overall Score (0-100)**: Weighted combination of all factors

## Database Storage

Scores are automatically saved to the `candidates` table:
- `experience_score`
- `skills_score`
- `education_score`
- `cultural_fit_score`
- `overall_score`
- `analysis_notes` - AI-generated strengths, weaknesses, and recommendation

## Cost Optimization

- Uses **Claude 3 Haiku** - cheapest Claude model (~$0.25 per 1M input tokens)
- Structured JSON output for reliable parsing
- Single API call per candidate

## Example Output

```json
{
  "candidate_id": 1,
  "candidate_name": "Emma Watson",
  "scores": {
    "experience_score": 85,
    "skills_score": 90,
    "education_score": 88,
    "cultural_fit_score": 82,
    "overall_score": 87,
    "strengths": "Strong full-stack experience with modern technologies",
    "weaknesses": "Limited leadership experience",
    "recommendation": "hire"
  },
  "status": "success"
}
```

## Adding New Positions

1. Add job description to `job_descriptions/your_position.md`
2. Add rubric to `rubrics/your_position_rubric.md`
3. Update position mapping in `ai_scorer.py`:

```python
position_map = {
    "Your Position": "your_position.md",
    # ... other positions
}
```

## Troubleshooting

### "No job description found"
- Check that the position name matches exactly
- Verify files exist in `job_descriptions/` and `rubrics/` folders

### "Invalid token"
- Verify `LAVA_FORWARD_TOKEN` in `.env` file
- Check token is valid in Lava dashboard

### "Insufficient balance"
- Add credits to your Lava wallet
- Each candidate scoring costs ~$0.001-0.002

## Tips

- Run scoring after adding new candidates
- Re-score candidates if job requirements change
- Use the dashboard to view updated scores
- Check `analysis_notes` for AI insights
