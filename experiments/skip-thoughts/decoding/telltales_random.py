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
X=['There is an annoying rat in our house.']
vectors = encoder.encode(X)
print("Input: " + X[0])
text1 =[]
text2 =[]
text3 =[]
text4 =[]

count =0
#vectors = encoder.encode(X)
text1 = horrortools.run_sampler(dec3, vectors, beam_width=1, stochastic=True, use_unk=False)
print("Horror: " + text1[0])

while(count < 20):
	vectors = encoder.encode(text1)
	text2 = adventuretools.run_sampler(dec2, vectors, beam_width=1, stochastic=True, use_unk=False)
	print("Adventure: " + text2[0])
	vectors = encoder.encode(text2)
	text3 = humortools.run_sampler(dec1, vectors, beam_width=1, stochastic=True, use_unk=False)
	print("Humor: " + text3[0])
	vectors = encoder.encode(text3)
        text4 = romancetools.run_sampler(dec4, vectors, beam_width=1, stochastic=True, use_unk=False)
        print("Romance: " + text4[0])
	vectors = encoder.encode(text4)
        text1 = horrortools.run_sampler(dec3, vectors, beam_width=1, stochastic=True, use_unk=False)
        print("Horror: " + text1[0])

	count = count + 1

print "THE END!!"


