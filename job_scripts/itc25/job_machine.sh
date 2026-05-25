#!/bin/bash
#SBATCH -p gpu_short       #Q
#SBATCH --gres=gpu:1 
#SBATCH -N  1        #node
#SBATCH -n  8        #proc
#SBATCH -c  1        #OMP_NUM_THREADS
#SBATCH -t 4:00:00
#SBATCH --output=output/%x-%j.out  

nvidia-smi

date
python3 ./../../src/main.py
date
