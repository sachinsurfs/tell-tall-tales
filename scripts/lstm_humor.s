#!/bin/bash

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=1

#SBATCH --cpus-per-task=1

#SBATCH --gres=gpu:k80:1

#SBATCH --time=20:00:00

#SBATCH --mem=8GB

#SBATCH --job-name=Adv_LSTM_language_test_

#SBATCH --mail-type=END

#SBATCH --mail-user=sds662@nyu.edu

#SBATCH --output=slurm_%j.out



module purge



SRCDIR=$HOME/

RUNDIR=$SCRATCH/run-${SLURM_JOB_ID/.*}

mkdir -p $RUNDIR

chmod -R 0777 $SCRATCH


cd $SLURM_SUBMIT_DIR

cp -r /scratch/sds662-share/Bi-LSTM/ $RUNDIR



cd $RUNDIR

module load python3/intel/3.6.3

module load cuda/9.0.176

module load pytorch/python3.6/0.3.0_4

module load cudnn/9.0v7.0.5

python3 $RUNDIR/Bi-LSTM/main.py --data $RUNDIR/Bi-LSTM/data/humor/ --cuda --emsize 600 --nhid 600 --dropout 0.65 --epochs 10 --tied  > $RUNDIR/lstm_humor_result_600

