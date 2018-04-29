from __future__ import print_function
import argparse
import os
import shutil
import random

parser = argparse.ArgumentParser()
parser.add_argument('--file', help="data file", default="train.txt")
args = parser.parse_args()


def generate_dataset(root):
    with open(data_file,"r") as f:
        sent = f.readlines()
        buffer = sent[0]
        if buffer.strip()=="":
            buffer = "Intro"
        with open("seq_"+data_file, "w") as f2:
            for s in sent[1:]:
                if s.strip()=="":
                    continue
                f2.write(buffer.strip() + '\t' + s.strip() + '\n')
                buffer = s

if __name__ == '__main__':
    data_file = args.file
    generate_dataset(data_file)
