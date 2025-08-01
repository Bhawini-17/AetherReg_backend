from pydantic import BaseModel
from typing import Optional

class ObligationMetadata(BaseModel):
    obligation_text: Optional[str] = None
    issuer: Optional[str] = None
    circular_id: Optional[str] = None
    effective_date: Optional[str] = None
    frequency: Optional[str] = None
    action_required: Optional[str] = None
    compliance_area: Optional[str] = None
    deadline: Optional[str] = None
    penalty: Optional[str] = None
    reference_clause: Optional[str] = None
