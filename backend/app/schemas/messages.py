from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class IncomingMessage(BaseModel):
    from_phone: str
    text: Optional[str] = None
    timestamp: Optional[str] = None
    message_id: Optional[str] = None
    message_type: Optional[str] = None
