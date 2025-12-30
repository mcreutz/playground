from prefect import flow, task


@task
def fetch_data():
    print("Step 1: Fetching data...")
    return [10, 20, 30, 40]


@task
def calculate_sum(data):
    print("Step 2: Calculating sum...")
    total = sum(data)
    print(f"Total: {total}")
    return total


@flow(log_prints=True)
def my_k8s_flow():
    data = fetch_data()
    result = calculate_sum(data)
    return result
