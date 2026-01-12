from __future__ import annotations

from dataclasses import dataclass

from app.schemas.messages import IncomingMessage


@dataclass(frozen=True)
class IntentResult:
    intent: str
    confidence: float
    raw_text: str


class IntentRouter:
    """
    Heurística simples (depois você troca por regras melhores / LLM / RAG etc).
    """

    def route(self, msg: IncomingMessage) -> IntentResult:
        text = (msg.text or "").strip()
        lowered = text.lower()

        if not text:
            return IntentResult(intent="empty", confidence=1.0, raw_text=text)

        if lowered in {"oi", "olá", "ola", "eae", "fala", "hello", "hi"}:
            return IntentResult(intent="greeting", confidence=0.9, raw_text=text)

        if "preço" in lowered or "preco" in lowered or "valor" in lowered:
            return IntentResult(intent="pricing", confidence=0.75, raw_text=text)

        if "ajuda" in lowered or "suporte" in lowered:
            return IntentResult(intent="support", confidence=0.75, raw_text=text)

        return IntentResult(intent="unknown", confidence=0.5, raw_text=text)
