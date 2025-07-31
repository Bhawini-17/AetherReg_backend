# aetherreg/obligation_schema.py

from pydantic import BaseModel
from typing import Optional

class ObligationMetadata(BaseModel):
    obligation_text: str
    issuer: Optional[str]
    circular_id: Optional[str]
    effective_date: Optional[str]
    frequency: Optional[str]
    action_required: Optional[str]
    compliance_area: Optional[str]
    deadline: Optional[str]
    penalty: Optional[str]
    reference_clause: Optional[str]
