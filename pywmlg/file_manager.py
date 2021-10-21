"""Classes and functions for reading and writing project files"""

from pathlib import Path
import pandas as pd


class FileManager:
    """Class for reading and writing project files"""

    def __init__(self, root_dir: Path) -> None:
        """Initialise the file manager by passing a root directory"""
        self.root_dir = root_dir

    def write_training_data_to_csv(self, training_data: pd.DataFrame) -> None:
        """Write training data to a CSV file"""
        filepath = self.root_dir / "training_data.csv"
        training_data.to_csv(filepath)

    def read_training_data_from_csv(self) -> pd.DataFrame:
        """Read training data from CSV file"""
        filepath = self.root_dir / "training_data.csv"
        return pd.read_csv(filepath)
