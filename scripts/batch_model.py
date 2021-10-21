"""Run models in batch mode"""

import typer


def run_batch(start: int, size: int):
    """Run a model batch"""
    print(f"running batch from {start} to {start + size}")


if __name__ == "__main__":
    typer.run(run_batch)
