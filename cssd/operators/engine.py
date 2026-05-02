class OperatorEngine:
    def __init__(self):
        self.operators = []

    def add(self, op):
        self.operators.append(op)

    def apply(self, query):
        prefix = "Rules:\n"
        for op in self.operators:
            prefix += f"- IF {op.condition} THEN {op.action}\n"

        return prefix + "\nQuery:\n" + query
