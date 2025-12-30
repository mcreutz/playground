import time
import random
from dagster import op, job, In


@op
def simulate_work() -> int:
    """Simulates work and returns a result."""
    time.sleep(random.uniform(0.1, 0.5))  # Simulate work
    return random.randint(1, 100)


@op(ins={"results": In(list)})
def collect_results(results) -> int:
    """Collects all results."""
    total = sum(results)
    print(f"Total result: {total}")
    return total


@job
def parallel_work():
    """Runs 50 work tasks in parallel and collects results."""
    work_results = [simulate_work() for _ in range(50)]
    collect_results(work_results)
    print(f"Total result: {work_results}")


if __name__ == "__main__":
    parallel_work()
