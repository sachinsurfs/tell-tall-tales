from nltk.corpus import wordnet as wn

def isNoun(x):
	nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
	return x in nouns

#print(isNoun('cook'))
