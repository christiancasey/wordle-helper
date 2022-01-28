import os
import pickle
import re
import numpy as np

wordle = pickle.load( open( "wordlist.p", "rb" ) )
total = len(wordle)

freq = []
for i in range(0,5):
    freq.append({})
    for j in range(ord('a'), ord('z')+1):
        freq[i][chr(j)] = 0

logprob = freq

for word in wordle:
    for i in range(0,5):
        freq[i][word[i]] += 1

for i in range(0,5):
    for j in range(ord('a'), ord('z')+1):
        logprob[i][chr(j)] = np.log(freq[i][chr(j)])

wordprob = [0] * total

for i, word in enumerate(wordle):
    prob = 0
    for j in range(0,5):
        prob += logprob[j][word[j]]
    
    wordle[i] = { 
        'word': word,
        'prob': prob,
    }

wordle.sort(key=lambda x: -x['prob'])

f = open('wordle.txt', 'w')
for word in wordle:
    f.write(word['word'] + '\n')
f.close()

print(wordle)

pickle.dump( wordle, open( "wordle.p", "wb" ) )



os.system('python play.py')

