from prefect import flow, task
from prefect_ray import RayTaskRunner
import ray


@task
def get_data():
    import pandas as pd, numpy as np

    return pd.DataFrame({"value": np.random.random(100)})


@task
def sklearn_process(data):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    return StandardScaler().fit_transform(data[["value"]])[:3].tolist()


@task
def scipy_process(data):
    import pandas as pd, scipy.stats as stats

    return stats.zscore(data["value"].values)[:3].tolist()


@task
def combine_results(sklearn_result, scipy_result):
    return {"sklearn": sklearn_result, "scipy": scipy_result}


@flow(task_runner=RayTaskRunner(address="ray://localhost:10001"))
def multi_tenant_pipeline():
    # Get data
    data = get_data()

    # Submit tasks to different Ray runtime environments
    sklearn_future = ray.remote(
        runtime_env={"pip": ["scikit-learn==1.3.0", "pandas==2.0.0"]}
    )(sklearn_process.fn).remote(data)

    scipy_future = ray.remote(runtime_env={"pip": ["scipy==1.11.0", "pandas==2.0.0"]})(
        scipy_process.fn
    ).remote(data)

    # Get results and combine
    sklearn_result = ray.get(sklearn_future)
    scipy_result = ray.get(scipy_future)

    return combine_results(sklearn_result, scipy_result)


if __name__ == "__main__":
    result = multi_tenant_pipeline()
    print(result)
