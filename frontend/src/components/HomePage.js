import React from 'react';
import './HomePage.css';

function HomePage({ onEnter }) {
  return (
    <div className="homepage">
      <div className="hero-section">
        <div className="hero-content">
          <div className="logo-animation">
            <div className="logo-circle"></div>
            <h1 className="hero-title">
              Recruit<span className="highlight">AI</span>
            </h1>
          </div>
          
          <p className="hero-subtitle">
            Transform the recruiting funnel from resumes to hires with AI-powered insights and real-time recruiter KPIs.
          </p>
          
          <button className="cta-button" onClick={onEnter}>
            Get Started
            <span className="arrow">→</span>
          </button>
        </div>
      </div>

      <div className="features-section">
        <div className="section-header">
          <h2 className="features-title">🚀 Features</h2>
          <div className="title-underline"></div>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🤖</div>
            <h3 className="feature-title">AI Recruiting Assistant</h3>
            <p className="feature-description">
              Chat with an AI to generate interview questions, analyze candidates, and get hiring advice
            </p>
            <div className="feature-shimmer"></div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📄</div>
            <h3 className="feature-title">Semantic Resume Processing</h3>
            <p className="feature-description">
              Deep understanding of resume content through semantic analysis, capturing the true meaning behind candidates' experience and skills
            </p>
            <div className="feature-shimmer"></div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3 className="feature-title">Pipeline Management</h3>
            <p className="feature-description">
              Track candidates through Resume Review, Phone Screen, Technical Interview, Final Round, and Offer stages
            </p>
            <div className="feature-shimmer"></div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📈</div>
            <h3 className="feature-title">Recruiter Dashboard</h3>
            <p className="feature-description">
              Visualize KPIs including hire rates, average scores, and pipeline breakdown
            </p>
            <div className="feature-shimmer"></div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">🏆</div>
            <h3 className="feature-title">Top 10 Applicants</h3>
            <p className="feature-description">
              Identify the best candidates for each KPI (overall, experience, skills)
            </p>
            <div className="feature-shimmer"></div>
          </div>

          <div className="feature-card">
            <div className="feature-icon">⚙️</div>
            <h3 className="feature-title">Dynamic and Real-time Scoring</h3>
            <p className="feature-description">
              Scores generated in real-time using keyword and semantic search algorithms with live analytics
            </p>
            <div className="feature-shimmer"></div>
          </div>
        </div>
      </div>

      <div className="cta-section">
        <div className="cta-content">
          <h2 className="cta-title">Ready to Transform Your Hiring Process?</h2>
          <p className="cta-text">Join the future of intelligent recruiting today.</p>
          <button className="cta-button-secondary" onClick={onEnter}>
            Launch Dashboard
            <span className="arrow">→</span>
          </button>
        </div>
      </div>

      <footer className="homepage-footer">
        <div className="footer-content">
          <p>© 2025 RecruitAI. Powered by AI to revolutionize your hiring.</p>
        </div>
      </footer>

      <div className="floating-shapes">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <div className="shape shape-3"></div>
        <div className="shape shape-4"></div>
      </div>
    </div>
  );
}

export default HomePage;

