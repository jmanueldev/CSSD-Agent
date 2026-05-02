class TrajectoryBuffer:
    def __init__(self, max_size=100):
        self.buffer = []
        self.max_size = max_size

    def add(self, traj):
        self.buffer.append(traj)
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)

    def sample(self, k=5):
        return self.buffer[-k:]
