# Migration Instructions for Rejection Feature

## Run this migration to add the rejection column to your existing database:

```bash
cd backend
python add_rejection_column.py
```

This will add the `is_rejected` column to the candidates table.

## Features Added:
- Toggle candidates as rejected/unrejected in the Dashboard table
- Rejected candidates show in red background
- Rejected candidates move to bottom of lists
- Rejected candidates excluded from Top Candidates view
- Stage dropdown disabled for rejected candidates
