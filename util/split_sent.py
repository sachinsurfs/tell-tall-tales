from __future__ import print_function
import argparse
import os
import shutil
import random

from nltk import sent_tokenize
 


parser = argparse.ArgumentParser()
parser.add_argument('--file', help="data file", default="train.txt")
args = parser.parse_args()


def generate_dataset(root):
    with open(data_file,"r") as f:
        sent = f.readlines()
        for s in sent:
        	ls = sent_tokenize(s)
        	for ss in ls:
        		print(ss)

if __name__ == '__main__':
    data_file = args.file
    generate_dataset(data_file)





