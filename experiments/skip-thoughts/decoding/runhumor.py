import sys

reload(sys)
sys.setdefaultencoding('latin-1')
sys.path.append('/home/jm7432/tell-tall-tales')
import skipthoughts
import trainHumor

X = []
file = open("/home/jm7432/big/Humor/humor-final.txt", "r")
for line in file:
        if len(line.strip())>0 and ("chapter" not in line or "part" not in line):
                X.append(line)

l = len(X)
Y = X[50:l-50]
Z = X[51:l-49]

model = skipthoughts.load_model()
trainHumor.trainer(Y,Z,model)
