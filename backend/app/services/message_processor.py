from __future__ import annotations

import logging
from typing import List

from app.schemas.messages import IncomingMessage
from app.schemas.webhook import WebhookPayload

logger = logging.getLogger(__name__)


class MessageProcessor:
    """
    Recebe o payload do webhook e extrai mensagens num formato interno estável.
    """

    def extract_messages(self, payload: WebhookPayload) -> List[IncomingMessage]:
        results: List[IncomingMessage] = []

        if not payload.entry:
            return results

        for entry in payload.entry:
            if not entry.changes:
                continue

            for change in entry.changes:
                value = change.value
                if not value or not value.messages:
                    continue

                for msg in value.messages:
                    from_phone = msg.from_ or ""
                    if not from_phone:
                        continue

                    text = None
                    if msg.type == "text" and msg.text:
                        text = msg.text.body

                    results.append(
                        IncomingMessage(
                            from_phone=from_phone,
                            text=text,
                            timestamp=msg.timestamp,
                            message_id=msg.id,
                            message_type=msg.type,
                        )
                    )

        return results
