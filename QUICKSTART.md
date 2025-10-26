# RecruitAI - Quick Start Guide

Get your hiring platform up and running in 5 minutes!

## 🚀 Quick Start

### Option 1: Automated (Recommended)

```bash
./start.sh
```

This will:
1. Install all dependencies
2. Initialize the database with sample data
3. Start backend (localhost:8000)
4. Start frontend (localhost:3000)

### Option 2: Manual Setup

#### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Start server
python main.py
```

#### Frontend Setup

```bash
# In a new terminal, navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

## 📱 Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🎯 Using the Application

### 1. Dashboard View
- View KPIs (total candidates, hire rate, average scores)
- See pipeline breakdown chart
- Review recent candidates with stage updates

### 2. Pipeline View
- Visualize candidates in each hiring stage
- See color-coded stages (Resume Review → Offer)
- Track candidate flow through the funnel

### 3. Top Candidates View
- Switch between metrics (Overall, Experience, Skills)
- See top 10 ranked candidates
- View detailed rankings table
- Read AI analysis for top candidate

### 4. Adding Candidates
Click "Add Candidate" button and fill in:
- Name
- Email
- Position
- Resume text (paste content)

The AI will automatically score the candidate!

## 📊 Sample Data

The database comes pre-loaded with:
- 2 recruiters: Sarah Johnson, Michael Chen
- 8 candidates across different stages
- Diverse experience levels and skill sets

## 🔧 Troubleshooting

### Port already in use?
```bash
# Backend
lsof -ti:8000 | xargs kill -9

# Frontend
lsof -ti:3000 | xargs kill -9
```

### Database issues?
```bash
cd backend
rm recruitai.db
python init_db.py
```

### Module not found?
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

## 🎨 Features

✅ AI-powered resume analysis  
✅ KPI tracking and visualization  
✅ Pipeline management  
✅ Top 10 candidates per metric  
✅ Real-time analytics  
✅ Beautiful modern UI  

## 📝 Tips

- Switch recruiters using the dropdown in the header
- Update candidate stages using the dropdown in the table
- Use Top Candidates view to identify best talent
- Check the AI analysis for insights

---

**Happy Recruiting! 🎉**

