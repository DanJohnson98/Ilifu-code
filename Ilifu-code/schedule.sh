#!/bin/bash

#SBATCH --job-name='lens_fitting'
#SBATCH --cpus-per-task=8
#SBATCH --mem=500
#SBATCH --output=testjob-%j-stdout.log
#SBATCH --error=testjob-%j-stderr.log
#SBATCH --time=00:30:00

source ~/.lenstronomyenv/bin/activate
echo "Submitting Slurm job"
python Doing_Fits_0.py