#!/bin/bash
#SBATCH -p GPU-S
#SBATCH --gres=gpu:1
#SBATCH -n 1
#SBATCH -t 72:00:00
#SBATCH -J example
#SBATCH -o output/%x-%j.out

nvidia-smi

date
python ./../../src/machin_like_formula.py
date
