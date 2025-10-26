import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function Dashboard({ recruiterId, candidates, onStageUpdate, onRejectToggle }) {
  const [kpis, setKpis] = useState(null);

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

  const kpiDefinitions = {
    totalCandidates: 'The total number of candidates currently in your recruitment pipeline across all stages.',
    hireRate: 'The percentage of candidates who successfully moved through the pipeline from initial resume review to receiving an offer.',
    avgExperience: 'The average experience score calculated by AI analysis of candidates\' work history, years of experience, and role progression.',
    avgSkills: 'The average skills score based on AI evaluation of technical skills, relevant competencies, and job-specific requirements.',
    avgOverall: 'The comprehensive average score combining experience, skills, and education metrics to provide an overall candidate quality assessment.'
  };

  if (!kpis) {
    return <div>Loading...</div>;
  }

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
            <div className="kpi-label">Total Candidates</div>
            <span className="info-icon" title={kpiDefinitions.totalCandidates}>ℹ️</span>
          </div>
          <div className="kpi-value">{kpis.total_candidates}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Hire Rate</div>
            <span className="info-icon" title={kpiDefinitions.hireRate}>ℹ️</span>
          </div>
          <div className="kpi-value">{kpis.conversion_rate}%</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Avg Experience Score</div>
            <span className="info-icon" title={kpiDefinitions.avgExperience}>ℹ️</span>
          </div>
          <div className="kpi-value">{kpis.average_scores.experience}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Avg Skills Score</div>
            <span className="info-icon" title={kpiDefinitions.avgSkills}>ℹ️</span>
          </div>
          <div className="kpi-value">{kpis.average_scores.skills}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Avg Overall Score</div>
            <span className="info-icon" title={kpiDefinitions.avgOverall}>ℹ️</span>
          </div>
          <div className="kpi-value">{kpis.average_scores.overall}</div>
        </div>
      </div>

      {kpis.scores_by_position && Object.keys(kpis.scores_by_position).length > 0 && (
        <div className="card">
          <h3>Average Scores by Job Category</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem' }}>
            {Object.entries(kpis.scores_by_position).map(([position, scores]) => (
              <div key={position} style={{ 
                padding: '1rem', 
                background: 'rgba(15, 23, 42, 0.6)', 
                borderRadius: '8px',
                borderLeft: '4px solid #667eea'
              }}>
                <h4 style={{ margin: '0 0 0.75rem 0', color: '#f1f5f9', fontSize: '1rem' }}>{position}</h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#cbd5e1', fontSize: '0.85rem' }}>Avg Experience:</span>
                    <strong style={{ color: '#667eea' }}>{scores.avg_experience}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#cbd5e1', fontSize: '0.85rem' }}>Avg Skills:</span>
                    <strong style={{ color: '#667eea' }}>{scores.avg_skills}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#cbd5e1', fontSize: '0.85rem' }}>Avg Overall:</span>
                    <strong style={{ color: '#667eea' }}>{scores.avg_overall}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '0.5rem', paddingTop: '0.5rem', borderTop: '1px solid rgba(100, 116, 139, 0.3)' }}>
                    <span style={{ color: '#cbd5e1', fontSize: '0.85rem' }}>Candidates:</span>
                    <strong style={{ color: '#f1f5f9' }}>{scores.count}</strong>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

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
                  <td>{candidate.name}</td>
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
    </div>
  );
}

export default Dashboard;

