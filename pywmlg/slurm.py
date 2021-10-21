"""Create slurm files in python"""

from pathlib import Path


def create_slurm_file(
    slurm_filepath: Path, batch_size: int, num_batches: int, time_limit: int
):
    """Return a slurm batch string"""
    slurm_string = f"""#!/usr/bin/bash
#SBATCH --job-name=pctsp
#SBATCH --partition=cpu-batch
#SBATCH --ntasks=10
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000
#SBATCH --time={time_limit}:00:00
#SBATCH --array=0-{num_batches-1}

## Loop over each batch ##
start=$(($SLURM_ARRAY_TASK_ID * {batch_size}))
srun --ntasks=1 python scripts/batch_model.py $start {batch_size} \
"""
    slurm_filepath.write_text(slurm_string)
