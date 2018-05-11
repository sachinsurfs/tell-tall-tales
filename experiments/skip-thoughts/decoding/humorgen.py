# -*- coding: latin-1 -*-
import humortools
import sys
sys.path.append('/home/jm7432/tell-tall-tales')
import skipthoughts
dec = humortools.load_model()
model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)
X=['What does most definitely matter is the Russian threat, except they ain’t so much a threat now as a promise since they managed to send their Sputnik into space.']
vectors = encoder.encode(X)
text = humortools.run_sampler(dec, vectors, beam_width=1, stochastic=False, use_unk=False)
print("Input: " + X[0])
print("Ouput: " + text[0])
