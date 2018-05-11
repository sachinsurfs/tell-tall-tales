import tools
import sys
sys.path.append('/home/jm7432/tell-tall-tales')
import skipthoughts
dec = tools.load_model()
model = skipthoughts.load_model()
encoder = skipthoughts.Encoder(model)
X=['but just one look at a minion sent him practically catatonic .']
vectors = encoder.encode(X)
text = tools.run_sampler(dec, vectors, beam_width=1, stochastic=False, use_unk=False)
print("Input: " + X[0])
print("Ouput: " + text[0])
