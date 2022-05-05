from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import spacy

nlp = spacy.load("pt_core_news_lg")
df = pd.read_csv('../filmes_dataset.csv', sep=',', usecols=['lancamento', 'titulo', 'descricao'])
idx = {}


class ActionProcurarFilme(Action):

    def name(self) -> Text:
        return "action_procurar_filme"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ultima_mensagem_usuario = tracker.latest_message['text']
        doc_mensagem = nlp(ultima_mensagem_usuario)

        for x in range(len(df['descricao'])):
            idx[x] = doc_mensagem.similarity(nlp(df['descricao'][x]))

        nome_filme = df['titulo'][max(idx, key=idx.get)]
        dispatcher.utter_message(
            template="utter_resposta_filme",
            nome_filme=nome_filme)

        return []
