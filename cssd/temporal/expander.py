import random
import copy

class TemporalExpander:
    def expand(self, traj, n_variants=3):
        variants = []

        for _ in range(n_variants):
            new_traj = copy.deepcopy(traj)

            for step in new_traj.steps:
                if random.random() < 0.3:
                    step.observation = "[PARTIAL] " + step.observation[:20]

                if random.random() < 0.2:
                    step.thought += " (uncertain)"

            variants.append(new_traj)

        return variants
