# app/engine/state.py
from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict

class WorkflowState(BaseModel):
    code: Optional[str] = None
    functions: List[str] = Field(default_factory=list)
    issues: int = 0
    quality_score: int = 0
    suggestions: List[str] = Field(default_factory=list)
    _next: Optional[str] = None
    _meta: Dict[str, Any] = Field(default_factory=dict)
