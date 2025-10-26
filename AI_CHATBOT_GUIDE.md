# AI Recruiting Assistant Chatbot

## Overview

The AI Recruiting Assistant is an intelligent chatbot that helps recruiters make better hiring decisions by providing expert advice on:

- **Interview Questions**: Generate tailored questions for specific roles and candidates
- **Candidate Analysis**: Get insights and recommendations on individual candidates  
- **Comparisons**: Compare multiple candidates side-by-side
- **Red Flags**: Identify potential concerns in candidates
- **Hiring Strategy**: Receive guidance on pipeline management and next steps

## Features

### 🎯 Context-Aware Conversations
The chatbot has access to your:
- Current recruiter profile
- All candidates in your pipeline
- Specific candidate details when selected
- Candidate scores and stages

### 💬 Natural Language Interface
- Chat naturally like talking to a colleague
- Get concise, conversational responses (not lengthy guides)
- Ask follow-up questions to dive deeper
- Reference previous conversations
- Get specific, actionable advice

### 📊 Data-Driven Insights
- Pulls real candidate data from your database
- Considers scores, stages, and experience levels
- Provides recommendations based on actual metrics

### ⚡ Quick Prompts
Pre-built prompts for common tasks:
- "Generate interview questions for a senior backend engineer"
- "What are common red flags to watch for in interviews?"
- "How should I structure my technical interview process?"
- "Compare my top 3 candidates"
- "Should I move forward with [candidate name]?"

## Setup

### Option 1: With AI API (Recommended)

1. **Get an API key** from one of these providers:
   - [OpenAI](https://platform.openai.com/api-keys) - for GPT-4 / GPT-3.5
   - [Anthropic](https://console.anthropic.com/) - for Claude

2. **Add to backend .env file**:
   ```bash
   # For OpenAI
   OPENAI_API_KEY=sk-...your-key-here...
   
   # OR for Anthropic
   ANTHROPIC_API_KEY=sk-ant-...your-key-here...
   ```

3. **Restart the backend**:
   ```bash
   cd backend
   source venv/bin/activate
   python main.py
   ```

### Option 2: Demo Mode (No API Key Required)

The chatbot works without an API key using intelligent mock responses! Perfect for:
- Testing the interface
- Demos and presentations
- Learning the feature

Mock responses are context-aware and provide realistic advice.

## Usage Guide

### Basic Usage

1. **Navigate to AI Assistant tab** in the app
2. **Select a candidate (optional)** from the dropdown for context-specific advice
3. **Type your question** or click a quick prompt
4. **Review the response** and ask follow-up questions

### Example Conversations

#### Generate Interview Questions

**You**: "Generate interview questions for a senior backend engineer"

**Assistant**: "Here are some interview questions for senior backend engineer:

1. Walk me through a complex technical problem you solved recently and your approach.
2. Tell me about a time you disagreed with a team member. How did you handle it?
3. How do you stay current with new technologies in your field?
4. Describe a project where you had to learn something completely new.

Would you like questions focused on a specific area?"

**You**: "Yes, focus on system design"

**Assistant**: Provides 3-4 targeted system design questions.

#### Analyze a Candidate

**You**: "Should I move forward with John Doe?" (with John selected in dropdown)

**Assistant**: "For John Doe at Phone Screen: If their scores are strong (>70), move them forward. If moderate (50-70), dig deeper in weak areas. If low (<50), consider passing unless there are exceptional circumstances.

What specific aspects would you like me to analyze?"

**You**: "What about their technical skills?"

**Assistant**: Provides focused analysis on technical skills.

#### Compare Candidates

**You**: "Compare my top 3 candidates for the backend role"

**Assistant**: "When comparing candidates, focus on: technical skills match, cultural fit, relevant experience, and growth potential. Create a simple scorecard (1-5) for each area and compare.

Who are the specific candidates you'd like me to compare?"

**You**: "John Doe and Jane Smith"

**Assistant**: Provides specific comparison between the two candidates.

#### Identify Red Flags

**You**: "What red flags should I look for in the interview tomorrow?"

**Assistant**: "Common red flags: frequent job hopping without reason, badmouthing former employers, inability to provide specific examples, inconsistencies between resume and interview, overly defensive about criticism, or lack of interest in growth.

One red flag isn't a dealbreaker, but multiple should give you pause. What specific concerns do you have?"

### Best Practices

1. **Provide Context**: Select a candidate from the dropdown for personalized advice
2. **Be Specific**: "Generate questions for Jane Smith's final interview" vs "Generate questions"
3. **Ask Follow-ups**: Dig deeper into any advice that needs clarification
4. **Reference Candidates**: Use actual candidate names from your pipeline
5. **Iterate**: Refine questions based on responses

## API Integration

### Backend Endpoint

```python
POST /api/chatbot/message
```

**Request:**
```json
{
  "message": "Generate interview questions for a senior backend engineer",
  "conversation_history": [
    {"role": "user", "content": "Previous message..."},
    {"role": "assistant", "content": "Previous response..."}
  ],
  "recruiter_id": 1,
  "candidate_id": 5  // optional
}
```

**Response:**
```json
{
  "response": "Here are tailored interview questions...",
  "timestamp": "2025-10-26T12:00:00",
  "provider": "openai"  // or "anthropic" or "mock"
}
```

### Context Provided to AI

The chatbot automatically receives:
- All candidates for the recruiter (up to 10 most recent)
- Selected candidate's full details (resume, scores, stage)
- Conversation history (last 10 messages)

## Customization

### Adding Your Own Prompts

Edit `frontend/src/components/ChatbotView.js`:

```javascript
const quickPrompts = [
  "Your custom prompt here",
  "Another prompt for your workflow",
  // ... more prompts
];
```

### Changing AI Models

Edit `backend/chatbot_service.py`:

```python
# For OpenAI - change model
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-3.5-turbo" for faster/cheaper
    # ...
)

# For Anthropic - change model  
response = client.messages.create(
    model="claude-3-sonnet-20240229",  # or "claude-3-opus" for best quality
    # ...
)
```

### Customizing System Prompt

Edit `backend/chatbot_service.py`:

```python
self.system_prompt = """Your custom instructions here...
Define the chatbot's role, tone, and expertise areas."""
```

## Troubleshooting

### Chatbot Returns "API Error"

**Problem**: API key is invalid or quota exceeded

**Solution**:
- Check API key in `.env`
- Verify API key has credits/quota remaining
- Check API provider status page

### Responses Are Too Generic

**Problem**: Not enough context provided

**Solution**:
- Select a candidate from dropdown
- Be more specific in your questions
- Reference actual candidate names
- Provide more details about the role

### Slow Responses

**Problem**: API latency or complex requests

**Solutions**:
- Use GPT-3.5 instead of GPT-4 (faster)
- Reduce conversation history depth
- Clear chat to reset context
- Check your internet connection

## Keyboard Shortcuts

- `Enter`: Send message
- `Shift + Enter`: New line in message

## Security & Privacy

### Data Handling
- Candidate data is only sent to AI when specifically queried
- API keys are stored securely in `.env` (never committed to git)
- Conversation history is local to the session
- No data is persisted beyond the conversation

### Best Practices
- Don't include sensitive personal information in queries
- Use candidate names or IDs, not SSNs or private data
- Review AI responses before making final decisions
- Keep API keys secure and rotate them regularly

## Mock Mode Features

When running without an API key, the chatbot provides:

✅ **Context-aware mock responses** based on your question type
✅ **Interview question templates** for common roles
✅ **Hiring decision frameworks** and best practices
✅ **Red flag checklists** from recruiting experts
✅ **Comparison methodologies** for evaluating candidates

Perfect for:
- Demos and presentations
- Training new recruiters
- Testing the interface
- Proof of concept

## Examples Library

### Technical Role Questions
```
"Generate system design questions for a senior engineer"
"What database questions should I ask?"
"How do I assess API design skills?"
```

### Behavioral Assessments
```
"Generate behavioral questions about teamwork"
"How do I assess cultural fit?"
"Questions about handling conflict"
```

### Candidate Evaluation
```
"Should I move forward with [candidate]?"
"Compare [candidate A] and [candidate B]"
"What are red flags for this candidate?"
"Is this candidate overqualified?"
```

### Process Optimization
```
"How should I structure my interview process?"
"What's the best way to screen resumes?"
"How many interview rounds should I have?"
"Tips for improving candidate experience"
```

## Future Enhancements

Planned features:
- 📧 Email templates for candidate outreach
- 📅 Interview scheduling suggestions
- 🎯 Compensation recommendations
- 📈 Historical hiring pattern analysis
- 🤝 Team fit assessments
- 📝 Offer letter assistance

## Support

For issues or feature requests:
1. Check this guide
2. Review backend logs: `backend/logs/`
3. Check API provider status
4. Review console errors in browser

## Cost Estimates

### OpenAI Pricing (approximate)
- GPT-3.5-Turbo: ~$0.001 per conversation
- GPT-4: ~$0.03 per conversation

### Anthropic Pricing (approximate)
- Claude Haiku: ~$0.001 per conversation
- Claude Sonnet: ~$0.015 per conversation

*Actual costs depend on conversation length and context*

## Tips for Best Results

1. **Be Conversational**: Ask natural questions like talking to a colleague
2. **Provide Context**: More details = better advice
3. **Iterate**: Ask follow-ups to refine the guidance
4. **Combine Tools**: Use chatbot alongside candidate scores and pipeline views
5. **Trust But Verify**: Use AI as an advisor, not a replacement for judgment

---

**Built with ❤️ for better hiring decisions**

