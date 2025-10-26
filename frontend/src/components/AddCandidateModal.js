import React, { useState } from 'react';

function AddCandidateModal({ recruiterId, onClose, onAdd }) {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    position: '',
    resume_text: '',
    recruiter_id: recruiterId
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd(formData);
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Add New Candidate</h2>
          <button className="close-btn" onClick={onClose}>×</button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Candidate Name *</label>
            <input
              type="text"
              id="name"
              name="name"
              required
              value={formData.name}
              onChange={handleChange}
              placeholder="John Doe"
            />
          </div>

          <div className="form-group">
            <label htmlFor="email">Email *</label>
            <input
              type="email"
              id="email"
              name="email"
              required
              value={formData.email}
              onChange={handleChange}
              placeholder="john.doe@example.com"
            />
          </div>

          <div className="form-group">
            <label htmlFor="position">Position *</label>
            <input
              type="text"
              id="position"
              name="position"
              required
              value={formData.position}
              onChange={handleChange}
              placeholder="Software Engineer"
            />
          </div>

          <div className="form-group">
            <label htmlFor="resume_text">Resume Text *</label>
            <textarea
              id="resume_text"
              name="resume_text"
              required
              value={formData.resume_text}
              onChange={handleChange}
              placeholder="Paste resume content here for AI analysis..."
            />
          </div>

          <div className="modal-actions">
            <button type="button" onClick={onClose} className="btn-secondary">
              Cancel
            </button>
            <button type="submit" className="btn-primary">
              Add Candidate & Analyze
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default AddCandidateModal;

