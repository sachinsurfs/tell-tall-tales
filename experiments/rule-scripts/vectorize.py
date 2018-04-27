import numpy as np
import pickle

def loadGloveModel(gloveFile):
    print "Loading Glove Model"
    f = open(gloveFile,'r')
    model = {}
    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print "Done.",len(model)," words loaded!"
    return model

model = loadGloveModel('./glove.6B.300d.txt')
pickle.dump( model, open( "glove.pkl", "wb" ) )



