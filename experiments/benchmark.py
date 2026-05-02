def run_benchmark(agent, tasks):
    results = []
    for t in tasks:
        results.append(agent.run(t))
    return results
