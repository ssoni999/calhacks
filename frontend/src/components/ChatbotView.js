import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './ChatbotView.css';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const ChatbotView = ({ recruiterId, candidates }) => {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: "👋 Hi! I'm your AI recruiting assistant. I can help you with:\n\n🎯 **Interview Questions** - Generate tailored questions for candidates\n📊 **Candidate Analysis** - Get insights on specific candidates\n⚖️ **Comparisons** - Compare multiple candidates\n🚩 **Red Flags** - Identify potential concerns\n💼 **Hiring Strategy** - Get advice on next steps\n\nWhat would you like help with today?",
      timestamp: new Date().toISOString()
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedCandidate, setSelectedCandidate] = useState(null);
  const messagesEndRef = useRef(null);

  // Quick prompts for easy access
  const quickPrompts = [
    "Generate interview questions for a senior backend engineer",
    "Compare my top 3 candidates",
    "Should I move forward with [candidate name]?",
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async (messageText = null) => {
    const textToSend = messageText || inputMessage.trim();
    if (!textToSend) return;

    // Add user message to chat
    const userMessage = {
      role: 'user',
      content: textToSend,
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    try {
      // Prepare conversation history for API (skip the initial welcome message)
      const conversationHistory = messages
        .slice(1) // Skip first message (welcome message)
        .map(msg => ({
          role: msg.role,
          content: msg.content
        }));

      const response = await axios.post(`${API_BASE}/chatbot/message`, {
        message: textToSend,
        conversation_history: conversationHistory,
        recruiter_id: recruiterId,
        candidate_id: selectedCandidate
      });

      // Add assistant response
      const assistantMessage = {
        role: 'assistant',
        content: response.data.response,
        timestamp: response.data.timestamp
      };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Chatbot error:', error);
      const errorMessage = {
        role: 'assistant',
        content: "Sorry, I encountered an error. Please try again.",
        timestamp: new Date().toISOString(),
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const handleQuickPrompt = (prompt) => {
    setInputMessage(prompt);
  };

  const clearChat = () => {
    setMessages([
      {
        role: 'assistant',
        content: "Chat cleared! What would you like to discuss?",
        timestamp: new Date().toISOString()
      }
    ]);
  };

  const formatMessage = (content) => {
    // Simple markdown-like formatting
    return content
      .split('\n')
      .map((line, idx) => {
        // Bold
        if (line.match(/\*\*(.*?)\*\*/)) {
          return (
            <p key={idx} dangerouslySetInnerHTML={{
              __html: line.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            }} />
          );
        }
        // Headers
        if (line.startsWith('###')) {
          return <h4 key={idx}>{line.replace('###', '').trim()}</h4>;
        }
        if (line.startsWith('##')) {
          return <h3 key={idx}>{line.replace('##', '').trim()}</h3>;
        }
        // Bullet points
        if (line.trim().startsWith('-') || line.trim().startsWith('•')) {
          return <li key={idx}>{line.replace(/^[-•]\s*/, '')}</li>;
        }
        // Numbered lists
        if (line.match(/^\d+\./)) {
          return <li key={idx}>{line.replace(/^\d+\.\s*/, '')}</li>;
        }
        // Empty lines
        if (!line.trim()) {
          return <br key={idx} />;
        }
        // Regular text
        return <p key={idx}>{line}</p>;
      });
  };

  return (
    <div className="chatbot-view">
      <div className="chatbot-header">
        <div className="header-title">
          <h2>🤖 AI Recruiting Assistant</h2>
          <p>Get expert advice on hiring decisions</p>
        </div>
        <div className="header-controls">
          {candidates && candidates.length > 0 && (
            <select
              value={selectedCandidate || ''}
              onChange={(e) => setSelectedCandidate(e.target.value ? parseInt(e.target.value) : null)}
              className="candidate-selector"
            >
              <option value="">Select a candidate (optional)</option>
              {candidates.map(candidate => (
                <option key={candidate.id} value={candidate.id}>
                  {candidate.name} - {candidate.position}
                </option>
              ))}
            </select>
          )}
          <button onClick={clearChat} className="btn-secondary">
            Clear Chat
          </button>
        </div>
      </div>

      <div className="chatbot-container">
        <div className="chat-messages">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.role} ${message.isError ? 'error' : ''}`}
            >
              <div className="message-icon">
                {message.role === 'assistant' ? '🤖' : '👤'}
              </div>
              <div className="message-content">
                <div className="message-text">
                  {formatMessage(message.content)}
                </div>
                <div className="message-timestamp">
                  {new Date(message.timestamp).toLocaleTimeString()}
                </div>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="message assistant loading">
              <div className="message-icon">🤖</div>
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="quick-prompts">
          <div className="quick-prompts-label">💡 Quick Prompts:</div>
          <div className="quick-prompts-grid">
            {quickPrompts.map((prompt, idx) => (
              <button
                key={idx}
                onClick={() => handleQuickPrompt(prompt)}
                className="quick-prompt-btn"
              >
                {prompt}
              </button>
            ))}
          </div>
        </div>

        <div className="chat-input-container">
          <textarea
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask me anything about recruiting, interview questions, or candidate decisions..."
            className="chat-input"
            rows={2}
            disabled={isLoading}
          />
          <button
            onClick={() => sendMessage()}
            disabled={!inputMessage.trim() || isLoading}
            className="btn-send"
          >
            {isLoading ? 'Sending...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatbotView;

