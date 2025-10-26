# AI Recruiting Assistant Chatbot - Quick Start

## ✅ What Was Built

A conversational AI chatbot that helps recruiters with:
- 🎯 Generating interview questions
- 📊 Analyzing candidates
- ⚖️ Comparing candidates
- 🚩 Identifying red flags
- 💼 Providing hiring strategy advice

## 📁 Files Created

### Backend (2 files)
1. **`backend/chatbot_service.py`** (380+ lines)
   - Main chatbot logic and AI integration
   - Mock responses for demo mode
   - Context-aware conversation handling
   - OpenAI and Anthropic API support

2. **`backend/main.py`** (updated)
   - Added `/api/chatbot/message` endpoint
   - Integrates with candidate database
   - Provides context to chatbot

### Frontend (3 files)
3. **`frontend/src/components/ChatbotView.js`** (220+ lines)
   - Chat interface with message history
   - Quick prompt buttons
   - Candidate selection dropdown
   - Real-time messaging

4. **`frontend/src/components/ChatbotView.css`** (400+ lines)
   - Modern, gradient-based design
   - Smooth animations
   - Responsive layout
   - Beautiful message bubbles

5. **`frontend/src/App.js`** (updated)
   - Added "🤖 AI Assistant" tab
   - Navigation integration
   - Props passing

### Documentation
6. **`AI_CHATBOT_GUIDE.md`** - Complete usage guide

## 🚀 How to Use

### 1. Start the Backend
```bash
cd backend
source venv/bin/activate
python main.py
```

### 2. Start the Frontend
```bash
cd frontend
npm start
```

### 3. Use the Chatbot
1. Click "🤖 AI Assistant" tab
2. Type a question or click a quick prompt
3. Get instant AI-powered advice!

## 💡 Features

### Works Out of the Box! ✨
- **No API key required** - Uses intelligent mock responses
- **Context-aware** - Knows your candidates and pipeline
- **Quick prompts** - Pre-built questions for common tasks
- **Beautiful UI** - Modern chat interface with animations

### Optional: Connect Real AI

For enhanced AI capabilities, add to `backend/.env`:

```bash
# Option 1: OpenAI (GPT-4/GPT-3.5)
OPENAI_API_KEY=sk-your-key-here

# Option 2: Anthropic (Claude)
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Then restart the backend!

## 🎯 Example Questions

Try these in the chatbot:

**Interview Questions:**
- "Generate interview questions for a senior backend engineer"
- "What technical questions should I ask?"
- "Give me behavioral interview questions"

**Candidate Analysis:**
- "Should I move forward with [candidate name]?"
- "What are red flags to look for?"
- "Compare my top 3 candidates"

**Hiring Strategy:**
- "How should I structure my interview process?"
- "What's the best way to screen resumes?"
- "Tips for improving candidate experience"

## 🏗️ Architecture

```
User Question
     ↓
ChatbotView (Frontend)
     ↓
POST /api/chatbot/message
     ↓
chatbot_service.py (Backend)
     ↓
[If API key: OpenAI/Anthropic]
[If no key: Smart mock responses]
     ↓
Context from Database:
- Recruiter's candidates
- Selected candidate details
- Conversation history
     ↓
AI Response
     ↓
Display in Chat UI
```

## 🎨 UI Features

- **Message History**: Full conversation preserved
- **Typing Indicator**: Shows when AI is thinking
- **Quick Prompts**: 6 pre-built question templates
- **Candidate Selector**: Pick a candidate for context
- **Clear Chat**: Start fresh anytime
- **Auto-scroll**: Always shows latest messages
- **Markdown Support**: Bold text, lists, headers
- **Timestamps**: Track conversation flow
- **Responsive**: Works on mobile and desktop

## 🔧 Customization

### Add Custom Quick Prompts

Edit `frontend/src/components/ChatbotView.js`:

```javascript
const quickPrompts = [
  "Your custom prompt here",
  "Another one",
  // ... add more
];
```

### Change Chatbot Personality

Edit `backend/chatbot_service.py`:

```python
self.system_prompt = """You are a [your custom role]...
[your custom instructions]"""
```

### Use Different AI Model

Edit `backend/chatbot_service.py`:

```python
# For GPT-4
model="gpt-4"

# For Claude Sonnet
model="claude-3-sonnet-20240229"
```

## 📊 Mock Mode Examples

The chatbot works WITHOUT an API key and provides:

✅ Interview question templates  
✅ Candidate evaluation frameworks  
✅ Red flag checklists  
✅ Hiring strategy advice  
✅ Comparison methodologies  

Perfect for demos, testing, and proof-of-concept!

## 🎓 How Mock Responses Work

The chatbot analyzes your question and provides appropriate responses:

- Keywords "interview" + "question" → Generates interview questions
- Keywords "compare" → Provides comparison framework
- Keywords "move forward" or "hire" → Gives hiring decision advice
- Keywords "red flag" → Lists common concerns
- General questions → Provides overview of capabilities

All responses are context-aware if you've selected a candidate!

## 🔐 Security

- API keys stored in `.env` (never committed to git)
- Candidate data only sent when specifically queried
- Conversation history is local to session
- No data persistence beyond active chat

## 🚀 Next Steps

1. ✅ **Try it now** - Works immediately with mock responses
2. 🔑 **Add API key** (optional) - Get real AI power
3. 🎨 **Customize prompts** - Add your own quick questions
4. 📈 **Use in hiring** - Start getting AI-powered advice!

## 💰 Cost (If Using Real API)

- **OpenAI GPT-3.5**: ~$0.001 per conversation
- **OpenAI GPT-4**: ~$0.03 per conversation
- **Claude Haiku**: ~$0.001 per conversation
- **Claude Sonnet**: ~$0.015 per conversation

Mock mode = FREE! 💚

## 🐛 Troubleshooting

### "API Error" message
→ Check API key in `.env` and restart backend

### Responses are generic
→ Select a candidate from dropdown for context
→ Be more specific in questions

### Chatbot tab not showing
→ Clear browser cache and reload

## 📚 Full Documentation

See `AI_CHATBOT_GUIDE.md` for:
- Detailed API documentation
- Advanced customization
- Security best practices
- Complete examples library
- Cost optimization tips

## ✨ Key Benefits

1. **Instant Expertise**: Get recruiter advice 24/7
2. **Data-Driven**: Uses your actual candidate data
3. **Time-Saving**: Quick answers to common questions
4. **Consistent**: Same quality advice every time
5. **Learning Tool**: Great for training new recruiters
6. **Flexible**: Works with or without API keys

---

**Start using your AI recruiting assistant today!** 🚀

Navigate to the "🤖 AI Assistant" tab and ask your first question!

