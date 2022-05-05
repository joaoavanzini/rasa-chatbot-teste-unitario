import pytest

from rasa_sdk import Tracker
from rasa_sdk.types import TrackerState

from rasa_sdk.executor import CollectingDispatcher
from actions.services.action_procurar_filme import ActionProcurarFilme


@pytest.mark.asyncio
async def test_action_procurar_filme():
    action = ActionProcurarFilme()
    action.name()

    tracker = Tracker.from_dict(TrackerState(sender_id="sender",latest_message={"text":"Perdidão em marte"}))

    dispatcher = CollectingDispatcher()

    await action.run(dispatcher, tracker, {})
    assert dispatcher.messages[0].get("nome_filme") == "Perdido em marte"
