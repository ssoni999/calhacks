import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function Dashboard({ recruiterId, candidates, onStageUpdate }) {
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
          <div className="kpi-label">Total Candidates</div>
          <div className="kpi-value">{kpis.total_candidates}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Conversion Rate</div>
          <div className="kpi-value">{kpis.conversion_rate}%</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Avg Experience Score</div>
          <div className="kpi-value">{kpis.average_scores.experience}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Avg Skills Score</div>
          <div className="kpi-value">{kpis.average_scores.skills}</div>
        </div>
        <div className="kpi-card">
          <div className="kpi-label">Avg Overall Score</div>
          <div className="kpi-value">{kpis.average_scores.overall}</div>
        </div>
      </div>

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
              </tr>
            </thead>
            <tbody>
              {candidates.slice(0, 10).map(candidate => (
                <tr key={candidate.id}>
                  <td>{candidate.name}</td>
                  <td>{candidate.position}</td>
                  <td>
                    <select 
                      value={candidate.stage} 
                      onChange={(e) => onStageUpdate(candidate.id, e.target.value)}
                      style={{ padding: '0.5rem', borderRadius: '8px', border: '1px solid #ddd' }}
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

