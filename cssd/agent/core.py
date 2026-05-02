from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

from cssd.memory.buffer import TrajectoryBuffer
from cssd.temporal.expander import TemporalExpander
from cssd.invariants.extractor import InvariantExtractor
from cssd.operators.synthesizer import OperatorSynthesizer
from cssd.operators.engine import OperatorEngine

class CSSDAgent:
    def __init__(self, tools):
        self.llm = ChatOpenAI(temperature=0)
        self.agent = initialize_agent(tools, self.llm, agent="zero-shot-react-description")

        self.buffer = TrajectoryBuffer()
        self.expander = TemporalExpander()
        self.extractor = InvariantExtractor()
        self.synthesizer = OperatorSynthesizer()
        self.operator_engine = OperatorEngine()

    def run(self, query):
        enhanced_query = self.operator_engine.apply(query)
        result = self.agent.run(enhanced_query)

        return result
