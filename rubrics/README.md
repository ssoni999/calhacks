# Assessment Rubrics

Comprehensive scoring rubrics for evaluating candidates across different engineering roles. Each rubric provides structured criteria for assessing candidates using keyword matching and semantic search from resumes.

## Available Rubrics

### 1. Software Engineer - Full Stack
**File:** `software_engineer_rubric.md`  
**Level:** Mid (3-5 years)

**Scoring Weights:**
- Experience: 30%
- Technical Skills: 40%
- Education: 15%
- Projects/Impact: 10%
- Soft Skills: 5%

**Key Assessment Areas:** Full-stack development, React, Python/Node.js, databases, cloud platforms

---

### 2. Senior Software Engineer - Backend/Infrastructure
**File:** `senior_software_engineer_rubric.md`  
**Level:** Senior (6-8 years)

**Scoring Weights:**
- Experience & Seniority: 35%
- Technical Skills: 35%
- System Design: 15%
- Leadership: 10%
- Education: 5%

**Key Assessment Areas:** Distributed systems, microservices, system design, leadership, cloud architecture

---

### 3. Frontend Engineer - React Specialist
**File:** `frontend_engineer_rubric.md`  
**Level:** Mid (3-6 years)

**Scoring Weights:**
- Frontend Technical: 45%
- React Expertise: 25%
- Experience: 20%
- Design/UX: 5%
- Education: 5%

**Key Assessment Areas:** React, TypeScript, CSS, responsive design, accessibility, UI/UX

---

### 4. DevOps Engineer - Cloud Infrastructure
**File:** `devops_engineer_rubric.md`  
**Level:** Mid-Senior (4-8 years)

**Scoring Weights:**
- Cloud Platforms: 35%
- Containers & Orchestration: 25%
- Automation & IaC: 20%
- Monitoring & Reliability: 10%
- Experience: 10%

**Key Assessment Areas:** AWS, Kubernetes, Terraform, CI/CD, monitoring, automation

---

### 5. Data Engineer - Big Data & Analytics
**File:** `data_engineer_rubric.md`  
**Level:** Mid-Senior (4-8 years)

**Scoring Weights:**
- Big Data & Processing: 35%
- Data Engineering Skills: 30%
- Cloud Data Platforms: 20%
- Experience: 10%
- Education: 5%

**Key Assessment Areas:** Spark, SQL, ETL, data pipelines, Airflow, data warehouses

---

## Scoring System

### Universal Scoring Scale (0-100)

All rubrics use a consistent 0-100 point scale for each category:

| Score | Assessment | Description |
|-------|-----------|-------------|
| 90-100 | Exceptional | Exceeds all requirements, expert-level |
| 80-89 | Strong | Exceeds most requirements, highly proficient |
| 70-79 | Good | Meets all requirements, solid performer |
| 60-69 | Moderate | Meets some requirements, gaps present |
| 50-59 | Below Bar | Significant gaps in requirements |
| 0-49 | Not Qualified | Does not meet minimum requirements |

### Overall Score Calculation

Each rubric calculates an **Overall Score** using weighted categories:

```
Overall Score = (Category1 × Weight1) + (Category2 × Weight2) + ... + (CategoryN × WeightN)
```

### Decision Thresholds

| Overall Score | Decision | Action |
|--------------|----------|--------|
| 90-100 | Strong Hire | Fast-track to final rounds |
| 80-89 | Hire | Proceed with interviews |
| 70-79 | Consider | Additional screening recommended |
| 60-69 | Maybe | Depends on specific needs |
| 50-59 | Likely No | Significant gaps present |
| 0-49 | No | Does not meet requirements |

---

## How to Use These Rubrics

### 1. Keyword Extraction
Each rubric includes **"Keywords to Look For"** sections that specify:
- Technical skills and technologies
- Experience indicators
- Impact and scale markers
- Education and certification keywords

### 2. Semantic Matching
Beyond keywords, use semantic search to identify:
- Equivalent technologies (e.g., "Redux" vs "state management")
- Similar concepts (e.g., "distributed systems" vs "scalable architecture")
- Impact descriptions (e.g., "improved performance" vs "optimized system")

### 3. Scoring Process

**Step 1: Extract Information**
- Parse resume for keywords and concepts
- Identify years of experience
- Note education and certifications
- Capture impact metrics

**Step 2: Score Each Category**
- Apply rubric criteria to each category
- Use keyword matches for initial scoring
- Apply semantic understanding for refinement
- Calculate category score (0-100)

**Step 3: Calculate Overall Score**
- Multiply each category score by its weight
- Sum weighted scores for overall score
- Apply any red flag deductions
- Add any bonus points

**Step 4: Make Decision**
- Compare overall score to thresholds
- Review specific category strengths/weaknesses
- Consider role-specific must-haves
- Make hire/no-hire recommendation

---

## Common Elements Across Rubrics

### Must-Have Requirements
Each rubric defines critical requirements that, if missing, cap the overall score (typically at 65-70). These ensure candidates meet minimum qualifications.

### Red Flags
Automatic point deductions for concerning patterns:
- Job hopping
- Large employment gaps
- Missing core skills for level
- No production experience

### Bonus Points
Additional points for exceptional qualifications:
- Advanced degrees
- Open source contributions
- Certifications
- Technical leadership
- Publications/speaking

---

## Role-Specific Considerations

### Software Engineer (Full Stack)
- **Critical:** React + Backend framework experience
- **Nice-to-have:** Full stack breadth
- **Watch for:** Backend or frontend only background

### Senior Software Engineer
- **Critical:** System design + leadership indicators
- **Nice-to-have:** Master's degree, publications
- **Watch for:** Years of experience vs. actual seniority level

### Frontend Engineer
- **Critical:** React expertise, responsive design
- **Nice-to-have:** Design sensibility, accessibility focus
- **Watch for:** Backend engineers trying to switch

### DevOps Engineer
- **Critical:** AWS + Kubernetes experience
- **Nice-to-have:** Certifications (AWS, CKA)
- **Watch for:** Sysadmin background without cloud/containers

### Data Engineer
- **Critical:** Spark + SQL proficiency
- **Nice-to-have:** Master's in Data Science, streaming experience
- **Watch for:** Data analyst vs. data engineer confusion

---

## Calibration Guidelines

### For Consistent Scoring

1. **Be Objective:** Use rubric criteria, not gut feeling
2. **Compare to Benchmarks:** Use example candidates as reference
3. **Weight Recent Experience:** Prioritize last 2-3 years
4. **Look for Growth:** Consider trajectory, not just current skills
5. **Context Matters:** Consider company size, tech stack evolution

### Common Pitfalls to Avoid

- **Resume Inflation:** Look for specifics, not buzzwords
- **Recency Bias:** Don't over-weight most recent role
- **Keyword Stuffing:** Verify depth beyond keyword matches
- **Title Inflation:** "Senior" at startup ≠ Senior at Big Tech
- **Education Bias:** Don't over-weight degrees vs. experience

---

## Integration with AI/ML Scoring

### Keyword Matching (40-50% accuracy)
- Extract keywords from resume
- Match against rubric keywords
- Count matches per category
- Initial score based on coverage

### Semantic Search (30-40% additional accuracy)
- Understand concept equivalence
- Identify related technologies
- Capture impact and context
- Refine initial keyword scores

### Manual Review (Final 10-20%)
- Verify top candidates
- Review borderline cases
- Assess qualitative factors
- Make final decision

### Recommended Workflow

```
Resume Input
    ↓
Keyword Extraction (automated)
    ↓
Semantic Analysis (AI/ML)
    ↓
Rubric Scoring (automated)
    ↓
Overall Score Calculation
    ↓
Score >= 70? → Manual Review → Interview
Score < 70? → Reject or Hold
```

---

## Example Scoring

### Sample Candidate: Emma Watson
**Role:** Software Engineer - Full Stack

**Extracted Information:**
- 5 years experience at Tech Solutions Inc
- React, Python, JavaScript, Django, Flask, PostgreSQL
- AWS deployment, Docker
- Bachelor's from Stanford
- Built apps serving 500k+ users

**Category Scores:**
- Experience: 85/100 (5 years, production experience)
- Technical Skills: 88/100 (React + Python + AWS)
- Education: 95/100 (Stanford CS degree)
- Projects/Impact: 85/100 (500k+ users, measurable impact)
- Soft Skills: 80/100 (collaboration, mentoring)

**Calculation:**
- 85 × 0.30 = 25.5
- 88 × 0.40 = 35.2
- 95 × 0.15 = 14.25
- 85 × 0.10 = 8.5
- 80 × 0.05 = 4.0

**Overall Score: 87.45** → **Strong Hire**

---

## Continuous Improvement

### Rubric Maintenance

1. **Review Quarterly:** Update for market changes, new technologies
2. **Calibrate with Hires:** Compare rubric scores to actual performance
3. **Adjust Weights:** Based on what predicts success
4. **Add New Keywords:** As technology evolves
5. **Refine Criteria:** Based on interview outcomes

### Feedback Loop

- Track rubric scores vs. interview performance
- Correlate scores with on-the-job success
- Identify false positives/negatives
- Adjust scoring criteria accordingly

---

## Files in This Directory

- `software_engineer_rubric.md` - Full Stack Engineer assessment
- `senior_software_engineer_rubric.md` - Senior Backend/Infrastructure assessment
- `frontend_engineer_rubric.md` - Frontend React Specialist assessment
- `devops_engineer_rubric.md` - DevOps Cloud Infrastructure assessment
- `data_engineer_rubric.md` - Data Engineering assessment
- `README.md` - This file

---

**Version:** 1.0  
**Last Updated:** October 2024  
**Maintained By:** Recruiting Team

## Questions?

For questions about using these rubrics or suggestions for improvements, contact the recruiting team.

