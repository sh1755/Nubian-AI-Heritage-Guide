# Nubian AI Heritage Guide

## Project Overview

The Nubian AI Heritage Guide is a small proof-of-concept project developed to demonstrate how historical archives and oral history transcripts can be transformed into an AI-powered conversational heritage assistant.

The project is inspired by the University of York's "Nubian Chronicles" project, which aims to digitally reconstruct submerged Lower Nubian villages and create AI-powered heritage experiences grounded in oral histories and archival records.

The current prototype demonstrates the AI workflow component and serves as the foundation for future integration with a 3D environment developed in Unity or Unreal Engine.

---

# Project Structure

```text
Nubian_AI_Heritage_Guide/
│
├── app.py
├── rag_engine.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── nubian_history.txt
│   └── oral_history.txt
│
└── assets/
```

---

# Tools Used

| Tool                | Purpose              |
| ------------------- | -------------------- |
| VS Code             | Code Development     |
| Python              | Programming Language |
| Streamlit           | Web Interface        |
| Ollama              | Local LLM Runtime    |
| Llama 3.2 / Mistral | Language Model       |
| Git                 | Version Control      |
| GitHub              | Project Hosting      |
| Future Unity/Unreal | 3D Environment       |

---

# Data Sources

## Nubian History Data

Contains:

* Nubian civilisation information
* Traditional architecture
* Agriculture and trade
* Nile River settlements
* Aswan High Dam impacts

## Oral History Data

Contains:

* Community memories
* Family traditions
* Storytelling
* Songs and weddings
* Relocation experiences
* Cultural heritage

---

# How the System Works

The system loads historical documents and oral history transcripts into a small knowledge base.

When a visitor asks a question:

1. The question is received.
2. The system loads relevant heritage information.
3. The question and context are sent to the language model.
4. The AI generates a grounded response.
5. The response is displayed to the visitor.

---

# Process Flow Diagram

```text
Nubian History Documents
            │
            ▼
     Knowledge Base
            ▲
            │
 Oral History Data
            │
            ▼

      User Question
            │
            ▼

      Python Engine
            │
            ▼

      Local LLM
     (Llama 3.2)
            │
            ▼

   AI Heritage Character
            │
            ▼

     Streamlit Interface
            │
            ▼

Future Unity / Unreal Environment
```

---

# Detailed Workflow

```text
Historical Archives
        +
Oral Histories
        │
        ▼
Data Collection
        │
        ▼
Text Cleaning
        │
        ▼
Knowledge Repository
        │
        ▼
User Question
        │
        ▼
Context Retrieval
        │
        ▼
Large Language Model
        │
        ▼
AI Character Response
        │
        ▼
Visitor Interaction
```

---

# Question and Answer Workflow

```text
Visitor
   │
   ▼
Asks Question
   │
   ▼
Streamlit Application
   │
   ▼
Knowledge Base Search
   │
   ▼
Relevant Historical Context
   │
   ▼
Llama 3.2 via Ollama
   │
   ▼
AI Response Generation
   │
   ▼
Answer Returned
   │
   ▼
Visitor Reads Response
```

---

# Example Questions

Question:

Who were the Nubian people?

Answer:

The Nubian people lived along the Nile River and are one of the oldest civilisations in Africa.

---

Question:

What were Nubian houses made from?

Answer:

Traditional Nubian houses were commonly built using mud bricks and decorated with colourful geometric patterns.

---

Question:

Why were villages submerged?

Answer:

Many Lower Nubian villages were submerged following the construction of the Aswan High Dam.

---

# Current Features

✔ Historical Knowledge Base

✔ Oral History Repository

✔ AI Conversational Agent

✔ Streamlit User Interface

✔ Local LLM Integration

✔ GitHub Portfolio Demonstration

✔ No Paid API Required

---

# Future Expansion

The current prototype focuses on AI workflows.

The future Nubian Chronicles architecture could include:

```text
3D Nubian Village
        │
        ▼
Interactive AI Character
        │
        ▼
Speech Recognition
        │
        ▼
RAG Knowledge Base
        │
        ▼
Large Language Model
        │
        ▼
Text-to-Speech
        │
        ▼
Immersive Heritage Experience
```

---

# Alignment with Nubian Chronicles

This project demonstrates:

* AI-powered heritage interaction
* Knowledge-grounded dialogue systems
* Oral history integration
* Historical archive processing
* Conversational AI workflows
* Future integration with Unity or Unreal Engine

The prototype serves as a foundation for transforming static digital heritage environments into interactive and intelligent cultural experiences.
