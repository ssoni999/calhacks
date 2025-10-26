
# RecruitAI - Streamlined Hiring Platform

Transform the recruiting funnel from resumes to hires with AI-powered insights and real-time recruiter KPIs.

## 🚀 Features

- **AI-Powered Resume Analysis**: Automatically score candidates using semantic search and keyword analysis
- **Detailed Resume Processing**: Comprehensive resume text analysis with extended candidate profiles
- **Pipeline Management**: Track candidates through Resume Review, Phone Screen, Technical Interview, Final Round, and Offer stages
- **Recruiter Dashboard**: Visualize KPIs including hire rates, average scores, and pipeline breakdown
- **Top 10 Applicants**: Identify the best candidates for each KPI (overall, experience, skills)
- **Real-time Analytics**: Charts and graphs for tracking recruiting performance
- **Modern UI**: Beautiful, responsive design with gradient themes
- **Dynamic Scoring**: Scores generated in real-time using keyword and semantic search algorithms

## 📁 Project Structure

```
calhacks/
├── backend/          # FastAPI backend
│   ├── main.py       # API endpoints
│   ├── models.py     # Database models
│   ├── schemas.py    # Pydantic schemas
│   ├── database.py   # Database configuration
│   └── init_db.py    # Initialize sample data
├── frontend/         # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.js
│   │   │   ├── CandidatesView.js
│   │   │   ├── KPIView.js
│   │   │   └── AddCandidateModal.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database with sample data:
```bash
python init_db.py
```

5. Start the FastAPI server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## 📖 API Endpoints

### Recruiters
- `GET /api/recruiters` - List all recruiters
- `GET /api/recruiters/{id}` - Get recruiter details
- `POST /api/recruiters` - Create a new recruiter

### Candidates
- `GET /api/candidates` - List all candidates (with optional filters)
- `POST /api/candidates` - Add a new candidate (with AI analysis)
- `PUT /api/candidates/{id}` - Update candidate stage or notes

### KPIs
- `GET /api/recruiters/{id}/kpis` - Get recruiter KPIs
- `GET /api/candidates/top-10` - Get top 10 candidates by metric

## 🎯 Usage

1. **View Dashboard**: See KPIs and pipeline overview
2. **Add Candidates**: Click "Add Candidate" and paste resume text
3. **Track Pipeline**: Navigate to Pipeline view to see candidates by stage
4. **Top Candidates**: View Top Candidates to see rankings by different metrics
5. **Update Stages**: Change candidate stages using the dropdown

## 🔍 How It Works

### AI Resume Analysis

The system analyzes resumes by:
- **Experience Score**: Based on relevant work history keywords
- **Skills Score**: Based on technical skills and technologies mentioned
- **Education Score**: Based on degree level and institution
- **Overall Score**: Weighted combination of all factors

### KPI Calculation

- **Total Candidates**: Number of candidates in the pipeline
- **Pipeline Breakdown**: Candidates in each stage
- **Average Scores**: Mean scores across all candidates
- **Hire Rate**: Percentage moving from resume to offer

## 🎨 Features Breakdown

### Dashboard View
- KPI cards with key metrics
- Pipeline bar chart
- Recent candidates table with stage updates

### Pipeline View
- Visual pipeline with 5 stages
- Drag-and-drop ready candidate cards
- Stage-specific color coding

### Top Candidates View
- Switchable metrics (overall, experience, skills)
- Bar chart visualization
- Detailed rankings table
- AI analysis for top candidate

## 🚧 Future Enhancements

- Voice cloning for interview scheduling
- Email integration for automated outreach
- Calendar integration for interview coordination
- Advanced resume parsing with PDF upload
- Team collaboration features
- Custom KPI calculations
- Export reports

## 📝 Sample Data

The database is initialized with:
- 2 recruiters (Sarah Johnson, Michael Chen)
- 8 candidates across different stages
- Detailed, comprehensive resume text for each candidate
- Scores will be generated through semantic search and keyword analysis (not pre-set)
- Varied experience levels and skill sets ranging from entry-level to senior positions

## 🤝 Contributing

This is a hackathon project. Feel free to fork and extend!

## 📄 License

MIT License

---

**Built for CalHacks 2024**
