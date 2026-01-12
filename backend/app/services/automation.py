from __future__ import annotations

import logging

from app.schemas.messages import IncomingMessage
from app.services.intent_router import IntentResult

logger = logging.getLogger(__name__)


class AutomationService:
    """
    Aqui vai viver a sua lógica.
    Por enquanto: só loga o que faria.
    """

    def handle(self, msg: IncomingMessage, intent: IntentResult) -> None:
        logger.info(
            "AUTOMATION: message received",
            extra={
                "from_phone": msg.from_phone,
                "intent": intent.intent,
                "confidence": intent.confidence,
                "message_id": msg.message_id,
                "message_type": msg.message_type,
            },
        )

        # “Ação” fake (só pra ver o pipeline funcionando)
        if intent.intent == "greeting":
            logger.info("AUTOMATION: would reply with greeting", extra={"to": msg.from_phone})
        elif intent.intent == "pricing":
            logger.info("AUTOMATION: would reply with pricing info", extra={"to": msg.from_phone})
        elif intent.intent == "support":
            logger.info("AUTOMATION: would reply with support instructions", extra={"to": msg.from_phone})
        elif intent.intent == "empty":
            logger.info("AUTOMATION: message had no text", extra={"to": msg.from_phone})
        else:
            logger.info("AUTOMATION: unknown intent", extra={"to": msg.from_phone})
