###############################################################################
# Language Modeling on Penn Tree Bank
#
# This file generates new sentences sampled from the language model
#
###############################################################################

import argparse

import torch
from torch.autograd import Variable

import data

parser = argparse.ArgumentParser(description='PyTorch Language Model')

# Model parameters.
parser.add_argument('--data', type=str, default='./data/',
                    help='location of the data corpus')
parser.add_argument('--Acheckpoint', type=str, default='./adventure.pt',
                    help='model checkpoint to use')
parser.add_argument('--Bcheckpoint', type=str, default='./horror.pt',
                    help='model checkpoint to use')
parser.add_argument('--Ccheckpoint', type=str, default='./humor.pt',
                    help='model checkpoint to use')

parser.add_argument('--outf', type=str, default='generated.txt',
                    help='output file for generated text')
parser.add_argument('--words', type=int, default='1000',
                    help='number of words to generate')
parser.add_argument('--seed', type=int, default=1111,
                    help='random seed')
parser.add_argument('--cuda', action='store_true',
                    help='use CUDA')
parser.add_argument('--temperature', type=float, default=1.0,
                    help='temperature - higher will increase diversity')
parser.add_argument('--log-interval', type=int, default=100,
                    help='reporting interval')
args = parser.parse_args()

# Set the random seed manually for reproducibility.
torch.manual_seed(args.seed)
if torch.cuda.is_available():
    if not args.cuda:
        print("WARNING: You have a CUDA device, so you should probably run with --cuda")
    else:
        torch.cuda.manual_seed(args.seed)

if args.temperature < 1e-3:
    parser.error("--temperature has to be greater or equal 1e-3")

with open(args.Acheckpoint, 'rb') as A:
    modelA = torch.load(A)

with open(args.Bcheckpoint, 'rb') as B:
    modelB = torch.load(B)

with open(args.Ccheckpoint, 'rb') as C:
    modelC = torch.load(C)

modelA.eval()
modelB.eval()
modelC.eval()


if args.cuda:
    modelA.cuda()
    modelB.cuda()
    modelC.cuda()

else:
    modelA.cpu()
    modelB.cpu()
    modelC.cpu()

corpusA = data.Corpus(args.data+'adventure')
corpusB = data.Corpus(args.data+'horror')
corpusC = data.Corpus(args.data+'humor')

ntokensA = len(corpusA.dictionary)
ntokensB = len(corpusB.dictionary)
ntokensC = len(corpusC.dictionary)


hiddenA = modelA.init_hidden(1)
hiddenB = modelB.init_hidden(1)
hiddenC = modelC.init_hidden(1)

input = Variable(torch.rand(1, 1).mul(ntokens).long(), volatile=True)
if args.cuda:
    input.data = input.data.cuda()

lenOfSentence = 10
noOfTurns = 100
model = modelA
curr = 'A'

with open(args.outf, 'w') as outf:
    for j in range(noOfTurns):
        if curr == 'A':
            model = modelB
            curr = 'B'
        else if curr == 'B':
            model = modelC
            curr = 'C'
        else if curr == 'C':
            model = modelA
            curr = 'A'
        outf.write(curr+": ", end="")
        for i in range(lenOfSentence):
            output, hidden = model(input, hidden)
            word_weights = output.squeeze().data.div(args.temperature).exp().cpu()
            word_idx = torch.multinomial(word_weights, 1)[0]
            input.data.fill_(word_idx)
            word = corpus.dictionary.idx2word[word_idx]

            outf.write(word + ' ')

            if i % args.log_interval == 0:
                print('| Generated {}/{} words'.format(i, args.words))
        outf.write('\n')

        