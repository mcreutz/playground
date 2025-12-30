from prefect import flow, task
import pandas as pd
import os

# Set Prefect server URL
os.environ["PREFECT_API_URL"] = "http://127.0.0.1:4200/api"


@task
def use_pandas():
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
    print(f"DataFrame:\n{df}")
    return len(df)


@flow
def simple_flow():
    count = use_pandas()
    print(f"Rows: {count}")


if __name__ == "__main__":
    # simple_flow()
    simple_flow.serve(name="pandas-deployment")
