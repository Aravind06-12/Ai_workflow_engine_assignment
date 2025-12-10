from pydantic import BaseModel

class CodeReviewRequest(BaseModel):
    code: str

class CodeReviewResponse(BaseModel):
    functions: dict
    complexity_report: dict
    issues: list
    suggestions: list
