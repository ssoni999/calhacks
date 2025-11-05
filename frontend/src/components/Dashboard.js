import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import CandidateProfileModal from './CandidateProfileModal';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function Dashboard({ recruiterId, candidates, onStageUpdate, onRejectToggle }) {
  const [kpis, setKpis] = useState(null);
  const [selectedPosition, setSelectedPosition] = useState('all');
  const [selectedCandidate, setSelectedCandidate] = useState(null);

  useEffect(() => {
    if (recruiterId) {
      fetchKPIs();
    }
  }, [recruiterId]);

  const fetchKPIs = async () => {
    try {
      const response = await axios.get(`${API_BASE}/recruiters/${recruiterId}/kpis`);
      setKpis(response.data);
    } catch (error) {
      console.error('Error fetching KPIs:', error);
    }
  };



  if (!kpis) {
    return <div>Loading...</div>;
  }

  // Get the selected position's skills score
  const getSelectedPositionSkillsScore = () => {
    if (selectedPosition === 'all' || !kpis.scores_by_position || !kpis.scores_by_position[selectedPosition]) {
      return kpis.average_scores.skills;
    }
    return kpis.scores_by_position[selectedPosition].avg_skills;
  };

  const selectedSkillsScore = getSelectedPositionSkillsScore();

  // Get available positions for dropdown
  const availablePositions = kpis.scores_by_position ? Object.keys(kpis.scores_by_position) : [];
  const allPositions = ['all', ...availablePositions];

  const pipelineData = [
    { stage: 'Resume Review', count: kpis.pipeline_breakdown.resume_review, fill: '#667eea' },
    { stage: 'Phone Screen', count: kpis.pipeline_breakdown.phone_screen, fill: '#f093fb' },
    { stage: 'Technical', count: kpis.pipeline_breakdown.technical_interview, fill: '#4facfe' },
    { stage: 'Final Round', count: kpis.pipeline_breakdown.final_round, fill: '#43e97b' },
    { stage: 'Offer', count: kpis.pipeline_breakdown.offers, fill: '#fa709a' }
  ];

  return (
    <div>
      <div className="kpi-grid">
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">
              Total Candidates
            </div>
          </div>
          <div className="kpi-value">{kpis.total_candidates}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">
              Hire Rate
            </div>
          </div>
          <div className="kpi-value">{kpis.conversion_rate}%</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">
              Avg Experience Score
            </div>
          </div>
          <div className="kpi-value">{kpis.average_scores.experience}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">
              Avg Skills Score
              {availablePositions.length > 0 && (
                <select 
                  value={selectedPosition} 
                  onChange={(e) => setSelectedPosition(e.target.value)}
                  onClick={(e) => e.stopPropagation()}
                  style={{ 
                    marginLeft: '0.5rem', 
                    padding: '0.25rem 0.5rem',
                    fontSize: '0.75rem',
                    borderRadius: '4px',
                    border: '1px solid rgba(100, 116, 139, 0.3)',
                    background: 'rgba(15, 23, 42, 0.6)',
                    color: '#cbd5e1',
                    cursor: 'pointer'
                  }}
                >
                  <option value="all">All Positions</option>
                  {availablePositions.map(pos => (
                    <option key={pos} value={pos}>{pos}</option>
                  ))}
                </select>
              )}
            </div>
          </div>
          <div className="kpi-value">{selectedSkillsScore}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">
              Avg Overall Score
            </div>
          </div>
          <div className="kpi-value">{kpis.average_scores.overall}</div>
        </div>
      </div>

      <div className="card">
        <h3>Pipeline Overview</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={pipelineData}>
            <CartesianGrid strokeDasharray="3 3" stroke="rgba(100, 116, 139, 0.3)" />
            <XAxis dataKey="stage" stroke="#cbd5e1" />
            <YAxis stroke="#cbd5e1" />
            <Tooltip contentStyle={{ background: 'rgba(15, 23, 42, 0.9)', border: '1px solid rgba(100, 116, 139, 0.3)', borderRadius: '8px', color: '#f1f5f9' }} cursor={{ fill: 'rgba(59, 130, 246, 0.1)' }} />
            <Legend wrapperStyle={{ color: '#cbd5e1' }} />
            <Bar dataKey="count" fill="#667eea" activeBar={{ fill: '#8b9aee' }} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="card">
        <h3>Recent Candidates</h3>
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Position</th>
                <th>Stage</th>
                <th>Overall Score</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              {candidates
                .sort((a, b) => (a.is_rejected === b.is_rejected ? 0 : a.is_rejected ? 1 : -1))
                .slice(0, 10)
                .map(candidate => (
                <tr key={candidate.id} style={{ opacity: candidate.is_rejected ? 0.5 : 1 }}>
                  <td>
                    <span 
                      onClick={() => setSelectedCandidate(candidate)}
                      style={{ cursor: 'pointer', color: '#667eea', textDecoration: 'underline' }}
                    >
                      {candidate.name}
                    </span>
                  </td>
                  <td>{candidate.position}</td>
                  <td>
                    <select 
                      value={candidate.stage} 
                      onChange={(e) => onStageUpdate(candidate.id, e.target.value)}
                      style={{ padding: '0.5rem', borderRadius: '8px', border: '1px solid rgba(100, 116, 139, 0.4)', background: 'rgba(15, 23, 42, 0.6)', color: '#f1f5f9' }}
                      disabled={candidate.is_rejected}
                    >
                      <option>Resume Review</option>
                      <option>Phone Screen</option>
                      <option>Technical Interview</option>
                      <option>Final Round</option>
                      <option>Offer</option>
                    </select>
                  </td>
                  <td>
                    <span className="candidate-score">{candidate.overall_score || 'Pending'}</span>
                  </td>
                  <td>
                    <button 
                      onClick={() => onRejectToggle(candidate.id, !candidate.is_rejected)}
                      style={{
                        padding: '0.5rem 1rem',
                        borderRadius: '8px',
                        border: 'none',
                        cursor: 'pointer',
                        background: candidate.is_rejected ? '#28a745' : '#dc3545',
                        color: 'white',
                        fontWeight: '600'
                      }}
                    >
                      {candidate.is_rejected ? 'Unreject' : 'Reject'}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {selectedCandidate && (
        <CandidateProfileModal 
          candidate={selectedCandidate} 
          onClose={() => setSelectedCandidate(null)} 
        />
      )}
    </div>
  );
}

export default Dashboard;

