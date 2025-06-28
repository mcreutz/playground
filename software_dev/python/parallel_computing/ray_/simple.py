# Simple Ray Cluster Demo
import ray
import time

# Initialize Ray with dashboard
ray.init(include_dashboard=True)
print(f"Dashboard: http://localhost:8265")


@ray.remote
def square(x):
    time.sleep(0.1)  # Simulate work
    return x**2


@ray.remote
def process_data(data, multiplier):
    return sum(x * multiplier for x in data)


# Example 1: Simple parallel tasks
numbers = [1, 2, 3, 4, 5]
futures = [square.remote(x) for x in numbers]
results = ray.get(futures)
print(f"Squared: {results}")

# Example 2: Different parameters
datasets = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
multipliers = [2, 3, 4]

futures = [process_data.remote(data, mult) for data, mult in zip(datasets, multipliers)]
results = ray.get(futures)
print(f"Processed: {results}")

print("Check the dashboard to see task execution!")
# ray.shutdown()
