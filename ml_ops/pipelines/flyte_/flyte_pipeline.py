from flytekit import task, workflow
import ray

ray.init(address="ray://localhost:65374")

@ray.remote
def square_remote(x):
    return x * x

@ray.remote
def sum_two_remote(a, b):
    return a + b

@ray.remote
def calculate_mean_remote(total, count):
    return total / count

@task
def square(x: int) -> int:
    return ray.get(square_remote.remote(x))

@task
def sum_two(a: int, b: int) -> int:
    return ray.get(sum_two_remote.remote(a, b))

@task
def calculate_mean(total: int, count: int) -> float:
    return ray.get(calculate_mean_remote.remote(total, count))

@task
def process_list(input_data: list[int]) -> float:
    # Step 1: Square each number
    squared_futures = [square_remote.remote(x) for x in input_data]
    
    # Step 2: Sum using reduce pattern
    total_future = squared_futures[0]
    for future in squared_futures[1:]:
        total_future = sum_two_remote.remote(total_future, future)
    
    # Step 3: Calculate mean
    mean_future = calculate_mean_remote.remote(total_future, len(input_data))
    
    return ray.get(mean_future)

@workflow
def pipeline() -> float:
    input_data = [1, 2, 3, 4, 5]
    result = process_list(input_data=input_data)
    return result

if __name__ == "__main__":
    result = pipeline()
    print(f"Mean of squares: {result}")