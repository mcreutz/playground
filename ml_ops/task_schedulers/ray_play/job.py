import ray

ray.init(address="auto")

@ray.remote
def process(x):
    return x * x

results = ray.get([process.remote(i) for i in range(5)])
print(f"Results: {results}")
