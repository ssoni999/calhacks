# Database Migration Instructions

## Run this migration to update your database schema:

```bash
cd backend
python migrate_db.py
```

This will add:
- `cultural_fit_score` column to the candidates table
- `is_rejected` column to the candidates table

## Features:
- Toggle candidates as rejected/unrejected in the Dashboard table
- Rejected candidates show with reduced opacity
- Rejected candidates move to bottom of lists
- Rejected candidates excluded from Top Candidates view
- Stage dropdown disabled for rejected candidates
