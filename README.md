# AI Workflow Engine Assignment  
### A Minimal Agent Workflow / Graph Execution Engine using FastAPI

This project implements a simplified workflow engine similar to LangGraph.  
It supports defining nodes, edges, shared state, conditional routing, loops, and a simple tool registry.  
An example workflow (**Code Review Mini-Agent**) is also implemented.

---

## 🚀 Features

### ✓ Workflow Engine
- Nodes = Python functions that read & modify shared state  
- Edges = Define execution order  
- Branching = Route to different nodes based on state values  
- Looping = Repeat a node until a condition is met  
- Shared State = Pydantic model flowing through nodes  

### ✓ Tool Registry
- Register Python functions as tools  
- Nodes can call tools dynamically  

### ✓ FastAPI Endpoints
- `POST /graph/create` → Create workflow graph  
- `POST /graph/run` → Execute workflow  
- `GET /graph/state/{run_id}` → Check current state  

### ✓ Example Workflow: Code Review Mini-Agent
Steps implemented:
1. Extract functions  
2. Check complexity  
3. Detect basic issues  
4. Suggest improvements  
5. Loop until `quality_score >= threshold`  

---

## 🗂 Folder Structure

Ai_workflow_engine_assignment/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # Request/response models
│ ├── db.py # In-memory storage for graphs & runs
│ ├── engine/
│ │ ├── state.py # Workflow state model
│ │ ├── graph.py # Graph class
│ │ ├── runner.py # Core workflow execution loop
│ │ └── registry.py # Tool registry
│ └── workflows/
│ └── code_review.py # Example workflow nodes
│
├── requirements.txt
└── README.md
---
