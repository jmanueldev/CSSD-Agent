from typing import List
from pydantic import BaseModel

class Step(BaseModel):
    thought: str
    action: str
    action_input: str
    observation: str

class Trajectory(BaseModel):
    steps: List[Step]
    goal: str

class Operator(BaseModel):
    name: str
    condition: str
    action: str
