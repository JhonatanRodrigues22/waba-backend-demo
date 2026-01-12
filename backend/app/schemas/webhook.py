from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class Text(BaseModel):
    body: Optional[str] = None


class Message(BaseModel):
    from_: Optional[str] = Field(default=None, alias="from")
    id: Optional[str] = None
    timestamp: Optional[str] = None
    type: Optional[str] = None
    text: Optional[Text] = None


class Value(BaseModel):
    messaging_product: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    contacts: Optional[List[Dict[str, Any]]] = None
    messages: Optional[List[Message]] = None
    statuses: Optional[List[Dict[str, Any]]] = None


class Change(BaseModel):
    field: Optional[str] = None
    value: Optional[Value] = None


class Entry(BaseModel):
    id: Optional[str] = None
    changes: Optional[List[Change]] = None


class WebhookPayload(BaseModel):
    object: Optional[str] = None
    entry: Optional[List[Entry]] = None
