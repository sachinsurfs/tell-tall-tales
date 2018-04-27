import pickle
model =  pickle.load( open( "glove.pkl", "rb" ) )
print("Pickle Loaded")
with open('train.txt') as f:
    content = f.readlines()

err = []
s = "This is a sentence test . I am ."
for s in content:
	for c in s.lower().split():
		if c not in model:
			err.append(c)
print(set(err))
