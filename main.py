import asyncio
import time
from typing import List

from async_runner import AsyncRunner


async def example_task(name: str, delay: float) -> str:
    """Example async task that simulates some work."""
    await asyncio.sleep(delay)
    return f"Task {name} completed after {delay} seconds"


async def example_error_task(name: str) -> None:
    """Example async task that raises an error."""
    raise ValueError(f"Simulated error in task {name}")


def run_single_coroutine_example() -> None:
    """Example of running a single coroutine."""
    print("\n=== Running Single Coroutine Example ===")
    result = AsyncRunner.run_coroutine(example_task, "A", 1.0)
    print(f"Result: {result}")


def run_multiple_coroutines_example() -> None:
    """Example of running multiple coroutines concurrently."""
    print("\n=== Running Multiple Coroutines Example ===")
    tasks = [
        (example_task, ("B", 2.0), {}),
        (example_task, ("C", 1.5), {}),
        (example_task, ("D", 1.0), {}),
    ]
    results = AsyncRunner.run_coroutines([task[0] for task in tasks], 
                                       *zip(*[task[1] for task in tasks]),
                                       **{k: v for task in tasks for k, v in task[2].items()})
    print(f"Results: {results}")


def run_error_handling_example() -> None:
    """Example of error handling in coroutines."""
    print("\n=== Running Error Handling Example ===")
    tasks = [
        (example_task, ("E", 1.0), {}),
        (example_error_task, ("F",), {}),
        (example_task, ("G", 0.5), {}),
    ]
    results = AsyncRunner.run_coroutines([task[0] for task in tasks],
                                       *zip(*[task[1] for task in tasks]))
    print(f"Results with error handling: {results}")


def main() -> None:
    """Main function demonstrating different uses of AsyncRunner."""
    print("AsyncRunner Examples\n")
    
    start_time = time.time()
    
    # Run examples
    run_single_coroutine_example()
    run_multiple_coroutines_example()
    run_error_handling_example()
    
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()