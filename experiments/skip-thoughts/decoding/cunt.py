import vocab
import cPickle as pkl
import numpy

with open('/home/jm7432/tell-tall-tales/decoding/humor_dict.pkl', 'rb') as f:
        worddict = pkl.load(f)
        wordcount = pkl.load(f)
sorted_idx = numpy.argsort(wordcount.values())[::-1]
words = wordcount.keys()
for idx, sidx in enumerate(sorted_idx):
	if idx>40000:
		print words[sidx] +":"+str(wordcount[words[sidx]])
		break
print len(sorted_idx)
	
print wordcount['The']
print wordcount['the']

