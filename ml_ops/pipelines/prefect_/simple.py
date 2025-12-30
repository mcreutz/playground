from prefect import flow, task
from prefect_ray import RayTaskRunner
import ray


# Task with pandas environment
@task
def extract_data():
    """Extract data - runs in pandas environment"""
    import pandas as pd
    import numpy as np

    data = pd.DataFrame({"id": range(1000), "value": np.random.random(1000)})
    return data  # Serialized as bytes between tasks


# Parallel processing with different Ray environments
@task
def process_chunk_a(data):
    """Process first half - runs in scikit-learn environment"""
    import pandas as pd
    from sklearn.preprocessing import StandardScaler

    chunk = data[:500]
    # Use scikit-learn functionality
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(chunk[["value"]])
    return pd.Series(scaled_values.flatten()[:5])  # Return small result


@task
def process_chunk_b(data):
    """Process second half - runs in numpy/scipy environment"""
    import pandas as pd
    import numpy as np

    chunk = data[500:]
    # Use numpy-heavy computation
    result = np.fft.fft(chunk["value"].values)
    return pd.Series(np.abs(result[:5]))  # Return small result


# Sequential task combining results
@task
def combine_results(result_a, result_b):
    """Combine parallel results - runs in pandas environment"""
    combined = pd.concat([result_a, result_b], axis=1)
    combined.columns = ["mean_values", "sum_values"]
    return combined


# Configure Ray workers with different environments
@ray.remote(runtime_env={"pip": ["pandas==2.0.0", "scikit-learn==1.3.0"]})
class SklearnWorker:
    def process(self, data):
        import pandas as pd
        from sklearn.preprocessing import StandardScaler

        chunk = data[:500]
        scaler = StandardScaler()
        scaled = scaler.fit_transform(chunk[["value"]])
        return pd.Series(scaled.flatten()[:5])


@ray.remote(runtime_env={"pip": ["pandas==2.0.0", "numpy==1.24.0", "scipy==1.10.0"]})
class NumpyWorker:
    def process(self, data):
        import pandas as pd
        import numpy as np

        chunk = data[500:]
        result = np.fft.fft(chunk["value"].values)
        return pd.Series(np.abs(result[:5]))


@flow(task_runner=RayTaskRunner(address="ray://localhost:10001"))
def simple_pipeline():
    """Simple pipeline with parallel and sequential steps"""

    # Sequential: Extract data
    raw_data = extract_data()

    # Parallel: Process in different Ray environments
    sklearn_worker = SklearnWorker.remote()
    numpy_worker = NumpyWorker.remote()

    result_a = ray.get(sklearn_worker.process.remote(raw_data))
    result_b = ray.get(numpy_worker.process.remote(raw_data))

    # Sequential: Combine results
    final_result = combine_results(result_a, result_b)

    return final_result


if __name__ == "__main__":
    # Run the pipeline
    result = simple_pipeline()
    print(f"Pipeline completed! Final result shape: {result.shape}")
