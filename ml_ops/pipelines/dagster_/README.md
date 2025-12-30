# Simple Dagster Parallel Work Example

This demonstrates:
1. A simple work function that sleeps and returns a random number
2. Running 5 of these in parallel
3. Collecting and summing the results

## How to run

```bash
cd software_dev/python/parallel_computing/dagster_
dagster job execute -f hello.py -j parallel_work
```

Or use the UI:
```bash
dagster dev -f hello.py
```
Then go to `http://localhost:3000` and run the `parallel_work` job.

## What it does

- 5 tasks run in parallel, each sleeping 0.1-0.5 seconds
- Each returns a random number 1-100
- Results are collected and summed
- Prints the total result 