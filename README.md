# 🇱🇰 Sinhala Multi-Agent Conversational Assistant 🤖

A web-based Sinhala NLP chatbot built using a Multi-Agent Architecture with Hybrid Intent Detection (TF-IDF + Logistic Regression).

This system demonstrates modular AI design, Sinhala language processing, and machine learning-based intent classification.

---

## Project Overview

This project implements a Sinhala conversational assistant using:

- Rule-based NLP preprocessing
- TF-IDF Vectorization
- Logistic Regression for intent classification
- Multi-Agent routing architecture
- Flask web interface
- Animated modern UI

The system processes Sinhala Unicode text and routes user queries to specialized conversational agents.

---

## 🧠 System Architecture

User Input  
↓  
Sinhala Text Processing  
↓  
TF-IDF Vectorization  
↓  
Logistic Regression Intent Classification  
↓  
Agent Router  
↓  
Specialized Agent  
↓  
Sinhala Response

---

## 🤖 Multi-Agent Design

Each agent has a single responsibility:

- Greeting Agent
- FAQ Agent (Library Info)
- University Info Agent
- Small Talk Agent
- Fallback Agent

This modular design improves scalability and maintainability.

---

## 📁 Project Structure

```
sinhala-multi-agent-chatbot/
│
├── app.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── intent/
│   ├── train_intent_model.py
│   └── intent_detector_ml.py
│
├── agents/
│   ├── greeting_agent.py
│   ├── faq_agent.py
│   ├── university_agent.py
│   ├── smalltalk_agent.py
│   └── fallback_agent.py
│
├── router/
│   └── agent_router.py
│
├── model/
│   ├── vectorizer.pkl
│   └── intent_model.pkl
│
└── README.md
```

---

## Technologies Used

- Python 3.x
- Flask
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- HTML5 / CSS3 (Glassmorphism UI)
- JavaScript (Fetch API)

---

---

## Machine Learning Details

- Feature Extraction: TF-IDF
- Classifier: Logistic Regression
- Balanced training dataset used
- Hybrid architecture (ML + rule-based fallback)

---

## Key Features

✅ Sinhala Unicode support  
✅ Multi-Agent architecture  
✅ Machine learning intent detection  
✅ Modular design  
✅ Animated modern UI  
✅ Extensible knowledge base

---

## Academic Relevance

This project demonstrates:

- Natural Language Processing concepts
- Intent Classification
- Text Vectorization
- Multi-Agent System Design
- Hybrid AI Architecture
- Modular Software Engineering

---

## Future Improvements

- Add confidence score threshold
- Add voice input
- Integrate Sinhala morphological analysis
- Deploy to cloud (Heroku / Render)
- Add database-based learning system

---

## Author

Dasun sandeepa

---

## Conclusion

This Sinhala Multi-Agent Conversational Assistant demonstrates a practical implementation of NLP techniques and machine learning in a modular AI system with a modern web interface.
