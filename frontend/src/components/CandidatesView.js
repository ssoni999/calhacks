import React from 'react';

function CandidatesView({ candidates, onStageUpdate }) {
  const stages = [
    { name: 'Resume Review', color: '#667eea' },
    { name: 'Phone Screen', color: '#f093fb' },
    { name: 'Technical Interview', color: '#4facfe' },
    { name: 'Final Round', color: '#43e97b' },
    { name: 'Offer', color: '#fa709a' }
  ];

  const getCandidatesByStage = (stage) => {
    return candidates
      .filter(c => c.stage === stage)
      .sort((a, b) => (a.is_rejected === b.is_rejected ? 0 : a.is_rejected ? 1 : -1));
  };

  return (
    <div>
      <div style={{ display: 'flex', gap: '1rem', overflowX: 'auto', paddingBottom: '1rem' }}>
        {stages.map(stage => (
          <div key={stage.name} className="pipeline-stage">
            <div className="stage-header" style={{ background: stage.color }}>
              {stage.name} ({getCandidatesByStage(stage.name).length})
            </div>
            <div className="stage-content">
              {getCandidatesByStage(stage.name).map(candidate => (
                <div 
                  key={candidate.id} 
                  className="candidate-item"
                  style={{ 
                    backgroundColor: candidate.is_rejected ? '#ffe6e6' : 'white',
                    opacity: candidate.is_rejected ? 0.7 : 1
                  }}
                >
                  <div className="candidate-name">
                    {candidate.name}
                    {candidate.is_rejected && <span style={{ color: '#dc3545', marginLeft: '0.5rem', fontSize: '0.85rem' }}>(Rejected)</span>}
                  </div>
                  <div className="candidate-email">{candidate.email}</div>
                  <div className="candidate-score">{candidate.overall_score || 'Pending'} pts</div>
                  {candidate.position && (
                    <div style={{ marginTop: '0.5rem', fontSize: '0.85rem', color: '#666' }}>
                      {candidate.position}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default CandidatesView;

