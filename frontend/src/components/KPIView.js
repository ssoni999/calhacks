import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function KPIView({ recruiterId }) {
  const [topCandidates, setTopCandidates] = useState([]);
  const [selectedMetric, setSelectedMetric] = useState('overall');

  useEffect(() => {
    if (recruiterId) {
      fetchTopCandidates();
    }
  }, [recruiterId, selectedMetric]);

  const fetchTopCandidates = async () => {
    try {
      const response = await axios.get(`${API_BASE}/candidates/top-10?recruiter_id=${recruiterId}&metric=${selectedMetric}`);
      setTopCandidates(response.data);
    } catch (error) {
      console.error('Error fetching top candidates:', error);
    }
  };

  const chartData = topCandidates.map((candidate, index) => ({
    name: candidate.name,
    overall: candidate.overall_score || 0,
    experience: candidate.experience_score || 0,
    skills: candidate.skills_score || 0,
    education: candidate.education_score || 0,
    rank: index + 1
  }));

  return (
    <div>
      <div className="card">
        <h3>Top 10 Candidates by KPI</h3>
        <div style={{ marginBottom: '1.5rem' }}>
          <select 
            value={selectedMetric} 
            onChange={(e) => setSelectedMetric(e.target.value)}
            style={{ 
              padding: '0.75rem', 
              borderRadius: '8px', 
              border: '1px solid #ddd',
              fontSize: '1rem',
              fontWeight: '600'
            }}
          >
            <option value="overall">Overall Score</option>
            <option value="experience">Experience Score</option>
            <option value="skills">Skills Score</option>
          </select>
        </div>

        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey={selectedMetric} fill="#667eea" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="card">
        <h3>Top 10 Detailed Rankings</h3>
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Position</th>
                <th>Stage</th>
                <th>Overall</th>
                <th>Experience</th>
                <th>Skills</th>
                <th>Education</th>
              </tr>
            </thead>
            <tbody>
              {topCandidates.map((candidate, index) => (
                <tr key={candidate.id}>
                  <td>
                    <span className="top-badge">#{index + 1}</span>
                  </td>
                  <td>{candidate.name}</td>
                  <td>{candidate.position}</td>
                  <td>{candidate.stage}</td>
                  <td>
                    <span className="candidate-score">{candidate.overall_score || 'Pending'}</span>
                  </td>
                  <td>{candidate.experience_score || 'Pending'}</td>
                  <td>{candidate.skills_score || 'Pending'}</td>
                  <td>{candidate.education_score || 'Pending'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {topCandidates.length > 0 && (
        <div className="card">
          <h3>AI Analysis for Top Candidate</h3>
          {topCandidates[0] && (
            <div style={{ padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
              <p style={{ marginBottom: '0.5rem', fontWeight: '600' }}>
                {topCandidates[0].name} - {topCandidates[0].position}
              </p>
              <p style={{ color: '#666', fontSize: '0.95rem' }}>
                {topCandidates[0].analysis_notes || 'Top performing candidate based on AI analysis.'}
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default KPIView;

