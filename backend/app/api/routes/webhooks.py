from __future__ import annotations

import os
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query, Request, Response

from app.schemas.webhook import WebhookPayload
from app.services.automation import AutomationService
from app.services.intent_router import IntentRouter
from app.services.message_processor import MessageProcessor

logger = logging.getLogger(__name__)
router = APIRouter()

# Serviços (simples assim por enquanto; depois a gente injeta via Depends)
processor = MessageProcessor()
router_intents = IntentRouter()
automation = AutomationService()


@router.get("/webhook")
def verify_webhook(
    hub_mode: Optional[str] = Query(default=None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(default=None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(default=None, alias="hub.challenge"),
):
    """
    Verificação do webhook (GET) no padrão do WhatsApp Cloud API / Meta.
    A Meta envia os params com ponto: hub.mode, hub.verify_token, hub.challenge
    e espera receber o hub.challenge como TEXTO PURO quando o token bater.
    """
    expected_token = os.getenv("WABA_VERIFY_TOKEN", "")

    if hub_mode == "subscribe" and hub_verify_token == expected_token and hub_challenge is not None:
        return Response(content=str(hub_challenge), media_type="text/plain")

    raise HTTPException(status_code=403, detail="Forbidden")


@router.post("/webhook")
async def receive_webhook(request: Request):
    """
    Recebimento de eventos (POST).
    Agora:
      1) tenta ler json
      2) valida/parseia no modelo
      3) extrai mensagens
      4) roteia intenção
      5) chama automações (só log por enquanto)
    """
    try:
        raw = await request.json()
    except Exception:
        raw = None

    if raw is None:
        logger.warning("WEBHOOK: invalid JSON (empty or not json)")
        return {"ok": True}

    # Parse/validação (sem quebrar o webhook se vier algo estranho)
    try:
        payload = WebhookPayload.model_validate(raw)
    except Exception as e:
        logger.exception("WEBHOOK: payload validation failed", extra={"error": str(e)})
        return {"ok": True}

    # Extrai mensagens e roda pipeline
    messages = processor.extract_messages(payload)
    logger.info("WEBHOOK: extracted messages", extra={"count": len(messages)})

    for msg in messages:
        intent = router_intents.route(msg)
        automation.handle(msg, intent)

    return {"ok": True}
