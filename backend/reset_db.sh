#!/bin/bash
echo "🗑️  Deleting database..."
rm -f recruitai.db
rm -f recruitai.db-shm
rm -f recruitai.db-wal

echo "📦 Creating fresh database..."
python init_db.py

echo "✅ Database reset complete!"
echo "   Run 'python run_ai_scoring.py' to score candidates"
