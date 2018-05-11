# -*- coding: latin-1 -*-
import humortools
import adventuretools
import horrortools
import romancetools

import sys
sys.path.append('/home/jm7432/tell-tall-tales')
import skipthoughts
dec1 = humortools.load_model()
dec2 = adventuretools.load_model()
dec3 = horrortools.load_model()
dec4 = romancetools.load_model()

model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)
X=['A misunderstanding alarms the home owner.']
moreX = ['Every night about twelve o’clock I slowly opened his door.', 'The old man was lying there not dreaming that I was at his door', 'For a whole hour I did not move.']
vectors = encoder.encode(X)
print("Input: " + X[0])
text1 =[]
text2 =[]
text3 =[]
text4 =[]

count =0
d = dict()

d[X[0]] = 1
#vectors = encoder.encode(X)
text1 = romancetools.run_sampler(dec4, vectors, beam_width=1, stochastic=False, use_unk=False)
print("Romance: " + text1[0])
d[text1[0]] = 1

def checkLoop(key):
	if key in d:
		return 1
	return 0 

while(count < 20):
	vectors = encoder.encode(text1)
	text2 = adventuretools.run_sampler(dec2, vectors, beam_width=1, stochastic=False, use_unk=False)
	print("Adventure: " + text2[0])
	if checkLoop(text2[0]):
		print("Loop")
		break
	d[text2[0]] = 1
	vectors = encoder.encode(text2)
	text3 = humortools.run_sampler(dec1, vectors, beam_width=1, stochastic=False, use_unk=False)
	print("Humor: " + text3[0])
        if checkLoop(text2[0]):
                print("Loop")
                break
	d[text3[0]] = 1
	vectors = encoder.encode(text3)
        text4 = romancetools.run_sampler(dec4, vectors, beam_width=1, stochastic=False, use_unk=False)
        print("Romance: " + text4[0])
        if checkLoop(text2[0]):
                print("Loop")
                break
	d[text4[0]] = 1
	vectors = encoder.encode(text4)
        text1 = horrortools.run_sampler(dec3, vectors, beam_width=1, stochastic=False, use_unk=False)
        print("Horror: " + text1[0])
        if checkLoop(text2[0]):
                print("Loop")
                break
	d[text1[0]] = 1
	#text1[0] = moreX[(count)%3]
        #print("Seed: "+ text1[0])
	count = count + 1

print "THE END!!"


