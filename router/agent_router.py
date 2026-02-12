from agents.greeting_agent import GreetingAgent
from agents.faq_agent import FAQAgent
from agents.university_agent import UniversityAgent
from agents.smalltalk_agent import SmallTalkAgent
from agents.fallback_agent import FallbackAgent

def route_agent(intent):
    if intent == "greeting":
        return GreetingAgent()
    elif intent == "faq":
        return FAQAgent()
    elif intent == "university":
        return UniversityAgent()
    elif intent == "smalltalk":
        return SmallTalkAgent()
    else:
        return FallbackAgent()
