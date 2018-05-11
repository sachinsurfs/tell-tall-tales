import sys

reload(sys)
sys.setdefaultencoding('latin-1')
sys.path.append('/home/jm7432/tell-tall-tales')

X = []
freq =0
file = open("/home/jm7432/big/Humor/humor-all.txt", "r")
for line in file:
	if len(line.strip())>0 and ("Chapter" in line):
		freq+=1

print(freq)

