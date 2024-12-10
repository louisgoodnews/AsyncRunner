# AsyncRunner

A Python utility for managing and executing asynchronous coroutines with ease. AsyncRunner provides a clean interface for running both single and multiple coroutines, with built-in error handling and logging capabilities.

## Features

- Run single or multiple coroutines concurrently
- Automatic event loop management
- Built-in error handling and logging
- Pydantic model-based configuration
- Type hints for better IDE support

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Here's a simple example of how to use AsyncRunner:

```python
from async_runner import AsyncRunner
import asyncio

# Define some example coroutines
async def example_coroutine(name: str, delay: int):
    await asyncio.sleep(delay)
    return f"Hello from {name}!"

# Run a single coroutine
result = AsyncRunner.run_coroutine(example_coroutine, "Coroutine 1", 1)

# Run multiple coroutines concurrently
coroutines = [
    example_coroutine("Coroutine 1", 1),
    example_coroutine("Coroutine 2", 2)
]
results = AsyncRunner.run_coroutines(coroutines)
```

## Requirements

- Python 3.9+
- pydantic 2.10+

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
