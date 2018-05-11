import vocab
import nltk

X = []
file = open("/home/jm7432/big/Romance/romance-final.txt","r")
for line in file:
        if len(line.strip())>0 and ("chapter" not in line or "part" not in line):
                X.append(line)


l=len(X)
Y=X[50:l-50]
worddict, wordcount = vocab.build_dictionary(Y)
vocab.save_dictionary(worddict, wordcount, '/home/jm7432/tell-tall-tales/decoding/romance_dict_final.pkl')
