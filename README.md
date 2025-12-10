# Ai_workflow_engine_assignment
Mini workflow engine for Tredence AI Engineering Internship Assignment
# Mini Workflow Engine (FastAPI) — Assignment Solution

This small project implements a minimal workflow/graph engine suitable for the coding assignment:
- Nodes are Python functions (async) that read & modify a shared state (Pydantic model).
- Edges define node sequencing.
- Branching is supported via `state._next`.
- Looping is supported by routing back to a previous node (via `_next`), with a safety max-step limit.
- Tool registry for shared helper functions.
- FastAPI endpoints to create and run graphs and check run state.

## Project structure
