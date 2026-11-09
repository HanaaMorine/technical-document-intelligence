from pydantic import BaseModel, Field, field_validator

class Requirement(BaseModel):
    requirement_id: str = Field(..., min_length=5)
    description: str = Field(..., min_length=10)
    category: str = Field(..., min_length=1)
    source_page: int = Field(..., ge=1)

    @field_validator('requirement_id')
    @classmethod
    def validate_requirement_id(cls, v):
        if not v.startswith("REQ-"):
            raise ValueError("requirement_id must start with 'REQ-'")
        return v

class RequirementExtraction(BaseModel):
    requirements:list[Requirement]
    