# Cluster Benchmarking


Usage:
- cd normal/
- For running the test without SLURM, run:
 $ python3  submit.py <int: Number of jobs to run> 
- For use with SLURM job manager, run:
 $ sbatch --array[1-TOTAL_JOBS] submit.sh

Glances was used for system monitoring.
