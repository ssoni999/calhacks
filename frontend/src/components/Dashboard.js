import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function Dashboard({ recruiterId, candidates, onStageUpdate, onRejectToggle }) {
  const [kpis, setKpis] = useState(null);
  const [tooltipStates, setTooltipStates] = useState({});

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

  const toggleTooltip = (kpiKey) => {
    setTooltipStates(prev => ({
      ...prev,
      [kpiKey]: !prev[kpiKey]
    }));
  };

  const kpiDefinitions = {
    totalCandidates: 'The total number of candidates currently in your recruitment pipeline across all stages.',
    conversionRate: 'The percentage of candidates who successfully moved through the pipeline from initial resume review to receiving an offer.',
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
            <button 
              className="info-icon" 
              onClick={() => toggleTooltip('totalCandidates')}
              aria-label="Show definition"
            >
              ℹ️
            </button>
          </div>
          <div className="kpi-value">{kpis.total_candidates}</div>
          {tooltipStates.totalCandidates && (
            <div className="kpi-tooltip">
              {kpiDefinitions.totalCandidates}
            </div>
          )}
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Conversion Rate</div>
            <button 
              className="info-icon" 
              onClick={() => toggleTooltip('conversionRate')}
              aria-label="Show definition"
            >
              ℹ️
            </button>
          </div>
          <div className="kpi-value">{kpis.conversion_rate}%</div>
          {tooltipStates.conversionRate && (
            <div className="kpi-tooltip">
              {kpiDefinitions.conversionRate}
            </div>
          )}
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Avg Experience Score</div>
            <button 
              className="info-icon" 
              onClick={() => toggleTooltip('avgExperience')}
              aria-label="Show definition"
            >
              ℹ️
            </button>
          </div>
          <div className="kpi-value">{kpis.average_scores.experience}</div>
          {tooltipStates.avgExperience && (
            <div className="kpi-tooltip">
              {kpiDefinitions.avgExperience}
            </div>
          )}
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Avg Skills Score</div>
            <button 
              className="info-icon" 
              onClick={() => toggleTooltip('avgSkills')}
              aria-label="Show definition"
            >
              ℹ️
            </button>
          </div>
          <div className="kpi-value">{kpis.average_scores.skills}</div>
          {tooltipStates.avgSkills && (
            <div className="kpi-tooltip">
              {kpiDefinitions.avgSkills}
            </div>
          )}
        </div>
        <div className="kpi-card">
          <div className="kpi-header">
            <div className="kpi-label">Avg Overall Score</div>
            <button 
              className="info-icon" 
              onClick={() => toggleTooltip('avgOverall')}
              aria-label="Show definition"
            >
              ℹ️
            </button>
          </div>
          <div className="kpi-value">{kpis.average_scores.overall}</div>
          {tooltipStates.avgOverall && (
            <div className="kpi-tooltip">
              {kpiDefinitions.avgOverall}
            </div>
          )}
        </div>
      </div>

      {kpis.scores_by_position && Object.keys(kpis.scores_by_position).length > 0 && (
        <div className="card">
          <h3>Average Scores by Job Category</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem' }}>
            {Object.entries(kpis.scores_by_position).map(([position, scores]) => (
              <div key={position} style={{ 
                padding: '1rem', 
                background: '#f8f9fa', 
                borderRadius: '8px',
                borderLeft: '4px solid #667eea'
              }}>
                <h4 style={{ margin: '0 0 0.75rem 0', color: '#333', fontSize: '1rem' }}>{position}</h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#666', fontSize: '0.85rem' }}>Avg Experience:</span>
                    <strong style={{ color: '#667eea' }}>{scores.avg_experience}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#666', fontSize: '0.85rem' }}>Avg Skills:</span>
                    <strong style={{ color: '#667eea' }}>{scores.avg_skills}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#666', fontSize: '0.85rem' }}>Avg Overall:</span>
                    <strong style={{ color: '#667eea' }}>{scores.avg_overall}</strong>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '0.5rem', paddingTop: '0.5rem', borderTop: '1px solid #dee2e6' }}>
                    <span style={{ color: '#666', fontSize: '0.85rem' }}>Candidates:</span>
                    <strong style={{ color: '#333' }}>{scores.count}</strong>
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
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="stage" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="count" fill="#667eea" />
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
                <tr key={candidate.id} style={{ backgroundColor: candidate.is_rejected ? '#ffe6e6' : 'transparent' }}>
                  <td>{candidate.name}</td>
                  <td>{candidate.position}</td>
                  <td>
                    <select 
                      value={candidate.stage} 
                      onChange={(e) => onStageUpdate(candidate.id, e.target.value)}
                      style={{ padding: '0.5rem', borderRadius: '8px', border: '1px solid #ddd' }}
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

