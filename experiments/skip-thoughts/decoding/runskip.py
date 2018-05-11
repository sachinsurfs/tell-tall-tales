import sys
sys.path.append('/home/jm7432/skip-thoughts')
import skipthoughts
import train

X = []
file = open("/home/jm7432/books_10_million", "r")
for line in file:
	X.append(line)

model = skipthoughts.load_model()
train.trainer(X,X,model)
