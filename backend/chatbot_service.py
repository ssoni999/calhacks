"""
AI Chatbot Service for Recruiter Assistance
Helps recruiters with interview questions, candidate analysis, and hiring decisions
"""
import os
from typing import List, Dict, Optional
from datetime import datetime
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# LLaVA Configuration (same as ai_scorer.py)
LAVA_TOKEN = os.getenv("LAVA_FORWARD_TOKEN")
LAVA_BASE_URL = os.getenv("LAVA_BASE_URL")
CLAUDE_HAIKU = "claude-3-haiku-20240307"

class RecruiterChatbot:
    """AI Chatbot to assist recruiters with hiring decisions"""
    
    def __init__(self):
        self.lava_token = LAVA_TOKEN
        self.lava_base_url = LAVA_BASE_URL
        self.has_api = bool(self.lava_token and self.lava_base_url)
        
        # System prompt that defines the chatbot's role
        self.system_prompt = """You are an expert technical recruiter and hiring consultant AI assistant. 

Your role is to help recruiters make better hiring decisions through natural conversation.

IMPORTANT RESPONSE GUIDELINES:
- Keep responses CONCISE and conversational (2-4 sentences typically)
- Answer the specific question asked, don't provide entire frameworks
- If asked for multiple items (e.g., interview questions), provide 3-4 examples max
- Use a natural, helpful tone - like a knowledgeable colleague
- Avoid lengthy formatted lists unless specifically requested
- Focus on actionable advice, not comprehensive guides
- If the question needs more context, ask a brief follow-up question

Your expertise areas:
• Generating focused interview questions
• Analyzing candidate qualifications
• Comparing candidates
• Providing hiring recommendations
• Sharing recruiting best practices

Be professional, data-driven, and practical. Give direct answers."""

    def generate_response(
        self, 
        message: str, 
        conversation_history: List[Dict[str, str]] = None,
        context: Optional[Dict] = None
    ) -> Dict:
        """
        Generate a chatbot response
        
        Args:
            message: User's message
            conversation_history: Previous messages in the conversation
            context: Additional context (candidates, job descriptions, etc.)
            
        Returns:
            Dictionary with response and metadata
        """
        if conversation_history is None:
            conversation_history = []
        
        # Build the full prompt with context
        enhanced_message = self._enhance_message_with_context(message, context)
        
        # Use LLaVA API if configured, otherwise use mock responses
        if self.has_api:
            response_text = self._call_llava_api(enhanced_message, conversation_history)
        else:
            response_text = self._generate_mock_response(message, context)
        
        return {
            "response": response_text,
            "timestamp": datetime.now().isoformat(),
            "provider": "llava" if self.has_api else "mock"
        }
    
    def _enhance_message_with_context(self, message: str, context: Optional[Dict]) -> str:
        """Add relevant context to the user's message"""
        if not context:
            return message
        
        enhanced = message + "\n\nContext:\n"
        
        if "candidates" in context:
            enhanced += f"\nCandidates under consideration:\n"
            for candidate in context["candidates"][:5]:  # Limit to 5 for token efficiency
                enhanced += f"- {candidate.get('name')}: {candidate.get('position')} "
                enhanced += f"(Experience: {candidate.get('experience_score', 0)}/100, "
                enhanced += f"Skills: {candidate.get('skills_score', 0)}/100)\n"
        
        if "job_description" in context:
            enhanced += f"\nJob Description: {context['job_description'][:500]}...\n"
        
        if "current_candidate" in context:
            candidate = context["current_candidate"]
            enhanced += f"\nCurrent Candidate: {candidate.get('name')}\n"
            enhanced += f"Position: {candidate.get('position')}\n"
            enhanced += f"Stage: {candidate.get('stage')}\n"
        
        return enhanced
    
    def _call_llava_api(self, message: str, history: List[Dict[str, str]]) -> str:
        """Call Claude via LLaVA API"""
        try:
            # Build conversation context
            conversation = f"{self.system_prompt}\n\n"
            
            # Add last 10 messages for context
            for msg in history[-10:]:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                conversation += f"\n{role.upper()}: {content}"
            
            # Add current message
            full_prompt = f"{conversation}\n\nUSER: {message}\n\nASSISTANT:"
            
            # Call Claude via LLaVA
            url = f"{self.lava_base_url}/forward?u=https://api.anthropic.com/v1/messages"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.lava_token}",
                "anthropic-version": "2023-06-01"
            }
            body = {
                "model": CLAUDE_HAIKU,
                "max_tokens": 500,  # Reduced to encourage concise responses
                "messages": [{"role": "user", "content": full_prompt}]
            }
            
            response = requests.post(url, headers=headers, json=body, timeout=30)
            response.raise_for_status()
            
            # Parse response
            result = response.json()
            return result["content"][0]["text"]
            
        except requests.exceptions.Timeout:
            return "⏱️ The request timed out. Please try again with a shorter question."
        except requests.exceptions.RequestException as e:
            error_detail = str(e)
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.text
                except:
                    pass
            print(f"LLaVA API Error: {error_detail}")
            # Fallback to mock response if LLaVA fails
            return self._generate_mock_response(message, {})
        except Exception as e:
            import traceback
            print(f"Unexpected error: {e}")
            print(traceback.format_exc())
            # Fallback to mock response
            return self._generate_mock_response(message, {})
    
    def _generate_mock_response(self, message: str, context: Optional[Dict]) -> str:
        """Generate a mock response when no API key is configured"""
        
        message_lower = message.lower()
        
        # Interview questions
        if "interview" in message_lower and "question" in message_lower:
            return self._generate_interview_questions_mock(context)
        
        # Candidate comparison
        elif "compare" in message_lower or "versus" in message_lower or "vs" in message_lower:
            return self._generate_comparison_mock(context)
        
        # Moving forward decision
        elif "move forward" in message_lower or "hire" in message_lower or "next step" in message_lower:
            return self._generate_hiring_decision_mock(context)
        
        # Red flags
        elif "red flag" in message_lower or "concern" in message_lower or "risk" in message_lower:
            return self._generate_red_flags_mock(context)
        
        # General advice
        else:
            return """I'm here to help with recruiting decisions! I can help with interview questions, candidate analysis, comparisons, and hiring strategy. What would you like to know?

*Note: Connect your API key in .env for enhanced AI capabilities*"""
    
    def _generate_interview_questions_mock(self, context: Optional[Dict]) -> str:
        """Mock interview question generation"""
        position = "the role"
        if context and "current_candidate" in context:
            position = context["current_candidate"].get("position", "the role")
        
        return f"""Here are some interview questions for {position}:

1. Walk me through a complex technical problem you solved recently and your approach.
2. Tell me about a time you disagreed with a team member. How did you handle it?
3. How do you stay current with new technologies in your field?
4. Describe a project where you had to learn something completely new.

Would you like questions focused on a specific area?"""
    
    def _generate_comparison_mock(self, context: Optional[Dict]) -> str:
        """Mock candidate comparison"""
        return """When comparing candidates, focus on: technical skills match, cultural fit, relevant experience, and growth potential. Create a simple scorecard (1-5) for each area and compare.

Who are the specific candidates you'd like me to compare?"""
    
    def _generate_hiring_decision_mock(self, context: Optional[Dict]) -> str:
        """Mock hiring decision advice"""
        if context and "current_candidate" in context:
            candidate = context["current_candidate"]
            name = candidate.get("name", "this candidate")
            stage = candidate.get("stage", "Resume Review")
            
            return f"""For {name} at {stage}: If their scores are strong (>70), move them forward. If moderate (50-70), dig deeper in weak areas. If low (<50), consider passing unless there are exceptional circumstances.

What specific aspects would you like me to analyze?"""
        
        return """Consider technical skills match, communication ability, cultural fit, and growth potential. If they score well on your must-haves, move forward. If there are coachable gaps, schedule another interview.

Who is the candidate you're evaluating?"""
    
    def _generate_red_flags_mock(self, context: Optional[Dict]) -> str:
        """Mock red flags analysis"""
        return """Common red flags: frequent job hopping without reason, badmouthing former employers, inability to provide specific examples, inconsistencies between resume and interview, overly defensive about criticism, or lack of interest in growth.

One red flag isn't a dealbreaker, but multiple should give you pause. What specific concerns do you have?"""


# Singleton instance
_chatbot_service = None

def get_chatbot_service() -> RecruiterChatbot:
    """Get or create chatbot service singleton"""
    global _chatbot_service
    if _chatbot_service is None:
        _chatbot_service = RecruiterChatbot()
    return _chatbot_service

