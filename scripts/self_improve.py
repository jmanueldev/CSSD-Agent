def self_improve(agent):
    trajectories = agent.buffer.sample()

    expanded = []
    for t in trajectories:
        expanded.extend(agent.expander.expand(t))

    invariants = agent.extractor.extract(expanded)
    op = agent.synthesizer.synthesize(invariants)

    agent.operator_engine.add(op)
