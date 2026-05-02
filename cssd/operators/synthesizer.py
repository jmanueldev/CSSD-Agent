from langchain.chat_models import ChatOpenAI

class OperatorSynthesizer:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

    def synthesize(self, invariants):
        prompt = f"""
Convert to operator:
{invariants}

Format:
Name:
Condition:
Action:
"""
        return self.llm.predict(prompt)
