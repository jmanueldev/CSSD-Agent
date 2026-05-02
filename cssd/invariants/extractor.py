from langchain.chat_models import ChatOpenAI

class InvariantExtractor:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0)

    def extract(self, trajectories):
        prompt = "Find invariant reasoning patterns:\n"

        for t in trajectories:
            for s in t.steps:
                prompt += f"{s.thought} | {s.action} | {s.observation}\n"

        return self.llm.predict(prompt)
