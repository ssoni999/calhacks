import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import Dashboard from './components/Dashboard';
import CandidatesView from './components/CandidatesView';
import KPIView from './components/KPIView';
import ChatbotView from './components/ChatbotView';
import AddCandidateModal from './components/AddCandidateModal';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function App() {
  const [recruiters, setRecruiters] = useState([]);
  const [selectedRecruiter, setSelectedRecruiter] = useState(null);
  const [candidates, setCandidates] = useState([]);
  const [view, setView] = useState('dashboard');
  const [showAddModal, setShowAddModal] = useState(false);

  useEffect(() => {
    fetchRecruiters();
  }, []);

  useEffect(() => {
    if (selectedRecruiter) {
      fetchCandidates(selectedRecruiter);
    }
  }, [selectedRecruiter]);

  const fetchRecruiters = async () => {
    try {
      const response = await axios.get(`${API_BASE}/recruiters`);
      setRecruiters(response.data);
      if (response.data.length > 0 && !selectedRecruiter) {
        setSelectedRecruiter(response.data[0].id);
      }
    } catch (error) {
      console.error('Error fetching recruiters:', error);
    }
  };

  const fetchCandidates = async (recruiterId) => {
    try {
      const response = await axios.get(`${API_BASE}/candidates?recruiter_id=${recruiterId}`);
      setCandidates(response.data);
    } catch (error) {
      console.error('Error fetching candidates:', error);
    }
  };

  const handleAddCandidate = async (candidateData) => {
    try {
      await axios.post(`${API_BASE}/candidates`, candidateData);
      fetchCandidates(selectedRecruiter);
      setShowAddModal(false);
    } catch (error) {
      console.error('Error adding candidate:', error);
      alert('Failed to add candidate. Please try again.');
    }
  };

  const handleStageUpdate = async (candidateId, newStage) => {
    try {
      await axios.put(`${API_BASE}/candidates/${candidateId}`, { stage: newStage });
      fetchCandidates(selectedRecruiter);
    } catch (error) {
      console.error('Error updating stage:', error);
    }
  };

  const handleRejectToggle = async (candidateId, isRejected) => {
    try {
      await axios.put(`${API_BASE}/candidates/${candidateId}`, { is_rejected: isRejected });
      fetchCandidates(selectedRecruiter);
    } catch (error) {
      console.error('Error toggling rejection:', error);
    }
  };

  const handleRecruiterChange = (e) => {
    setSelectedRecruiter(parseInt(e.target.value));
  };

  return (
    <div className="App">
      <header className="app-header">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div className="header-content">
            <h1>RecruitAI</h1>
            <p>Streamlined Hiring Platform</p>
          </div>
          <div className="header-controls">
            <select value={selectedRecruiter || ''} onChange={handleRecruiterChange}>
              {recruiters.map(recruiter => (
                <option key={recruiter.id} value={recruiter.id}>
                  {recruiter.name}
                </option>
              ))}
            </select>
            <button onClick={() => setShowAddModal(true)} className="btn-primary">
              + Add Candidate
            </button>
          </div>
        </div>
      </header>

      <nav className="app-nav">
        <button 
          className={view === 'dashboard' ? 'active' : ''} 
          onClick={() => setView('dashboard')}
        >
          Dashboard
        </button>
        <button 
          className={view === 'candidates' ? 'active' : ''} 
          onClick={() => setView('candidates')}
        >
          Pipeline
        </button>
        <button 
          className={view === 'chatbot' ? 'active' : ''} 
          onClick={() => setView('chatbot')}
        >
          🤖 AI Assistant
        </button>
        <button 
          className={view === 'kpi' ? 'active' : ''} 
          onClick={() => setView('kpi')}
        >
          Top Candidates
        </button>
      </nav>

      <main className="app-main">
        {view === 'dashboard' && (
          <Dashboard 
            recruiterId={selectedRecruiter} 
            candidates={candidates}
            onStageUpdate={handleStageUpdate}
            onRejectToggle={handleRejectToggle}
          />
        )}
        {view === 'candidates' && (
          <CandidatesView 
            candidates={candidates}
            onStageUpdate={handleStageUpdate}
          />
        )}
        {view === 'chatbot' && (
          <ChatbotView 
            recruiterId={selectedRecruiter}
            candidates={candidates}
          />
        )}
        {view === 'kpi' && (
          <KPIView 
            recruiterId={selectedRecruiter} 
          />
        )}
      </main>

      {showAddModal && (
        <AddCandidateModal
          recruiterId={selectedRecruiter}
          onClose={() => setShowAddModal(false)}
          onAdd={handleAddCandidate}
        />
      )}
    </div>
  );
}

export default App;

