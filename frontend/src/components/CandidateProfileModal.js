import React, { useEffect } from 'react';

function CandidateProfileModal({ candidate, onClose }) {
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);
  }, [onClose]);

  if (!candidate) return null;

  const getScoreColor = (score) => {
    if (!score) return '#94a3b8';
    if (score >= 80) return '#43e97b';
    if (score >= 60) return '#4facfe';
    if (score >= 40) return '#f093fb';
    return '#fa709a';
  };

  const getStrengths = () => {
    const scores = [
      { name: 'Experience', value: candidate.experience_score },
      { name: 'Skills', value: candidate.skills_score },
      { name: 'Education', value: candidate.education_score }
    ];
    return scores.filter(s => s.value && s.value >= 70).sort((a, b) => b.value - a.value);
  };

  const getWeaknesses = () => {
    const scores = [
      { name: 'Experience', value: candidate.experience_score },
      { name: 'Skills', value: candidate.skills_score },
      { name: 'Education', value: candidate.education_score }
    ];
    return scores.filter(s => s.value && s.value < 70).sort((a, b) => a.value - b.value);
  };

  const strengths = getStrengths();
  const weaknesses = getWeaknesses();

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()} style={{ maxWidth: '600px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '1.5rem' }}>
          <div>
            <h2 style={{ margin: 0, marginBottom: '0.5rem', color: '#f1f5f9' }}>{candidate.name}</h2>
            <p style={{ color: '#94a3b8', margin: 0 }}>{candidate.position}</p>
            <p style={{ color: '#64748b', fontSize: '0.9rem', margin: '0.25rem 0 0 0' }}>{candidate.email}</p>
          </div>
          <button onClick={onClose} style={{ background: 'none', border: 'none', fontSize: '1.5rem', cursor: 'pointer', color: '#cbd5e1' }}>×</button>
        </div>

        <div style={{ marginBottom: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{ fontWeight: '600', color: '#cbd5e1' }}>Overall Score</span>
            <span style={{ fontSize: '1.5rem', fontWeight: '700', color: getScoreColor(candidate.overall_score) }}>
              {candidate.overall_score || 'N/A'}
            </span>
          </div>
          <div style={{ background: 'rgba(15, 23, 42, 0.6)', borderRadius: '8px', height: '8px', overflow: 'hidden' }}>
            <div style={{ width: `${candidate.overall_score || 0}%`, height: '100%', background: getScoreColor(candidate.overall_score), transition: 'width 0.3s' }} />
          </div>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem', marginBottom: '1.5rem' }}>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.85rem', color: '#cbd5e1', marginBottom: '0.25rem' }}>Experience</div>
            <div style={{ fontSize: '1.25rem', fontWeight: '600', color: getScoreColor(candidate.experience_score) }}>
              {candidate.experience_score || 'N/A'}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.85rem', color: '#cbd5e1', marginBottom: '0.25rem' }}>Skills</div>
            <div style={{ fontSize: '1.25rem', fontWeight: '600', color: getScoreColor(candidate.skills_score) }}>
              {candidate.skills_score || 'N/A'}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '0.85rem', color: '#cbd5e1', marginBottom: '0.25rem' }}>Education</div>
            <div style={{ fontSize: '1.25rem', fontWeight: '600', color: getScoreColor(candidate.education_score) }}>
              {candidate.education_score || 'N/A'}
            </div>
          </div>
        </div>

        {strengths.length > 0 && (
          <div style={{ marginBottom: '1.5rem' }}>
            <h3 style={{ fontSize: '1rem', marginBottom: '0.75rem', color: '#43e97b' }}>✓ Strengths</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              {strengths.map(s => (
                <div key={s.name} style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem', background: 'rgba(67, 233, 123, 0.1)', borderRadius: '6px' }}>
                  <span style={{ color: '#cbd5e1' }}>{s.name}</span>
                  <span style={{ fontWeight: '600', color: '#43e97b' }}>{s.value}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {weaknesses.length > 0 && (
          <div style={{ marginBottom: '1.5rem' }}>
            <h3 style={{ fontSize: '1rem', marginBottom: '0.75rem', color: '#fa709a' }}>⚠ Areas for Development</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              {weaknesses.map(w => (
                <div key={w.name} style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem', background: 'rgba(250, 112, 154, 0.1)', borderRadius: '6px' }}>
                  <span style={{ color: '#cbd5e1' }}>{w.name}</span>
                  <span style={{ fontWeight: '600', color: '#fa709a' }}>{w.value}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        <div style={{ padding: '1rem', background: 'rgba(15, 23, 42, 0.6)', borderRadius: '8px', fontSize: '0.9rem', color: '#cbd5e1' }}>
          <strong>Current Stage:</strong> {candidate.stage}
        </div>
      </div>
    </div>
  );
}

export default CandidateProfileModal;
