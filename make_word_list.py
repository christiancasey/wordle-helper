import os
import pickle
import re

f = open('words_alpha.txt', 'r')

s = f.read()
words = s.splitlines()
f.close()

wordle = []
for word in words:
    if len(word) == 5:
        wordle.append(word)

pickle.dump( wordle, open( "wordlist.p", "wb" ) )

f = open('wordle.txt', 'w')
for word in wordle:
    f.write(word + '\n')
f.close()

print(wordle)


os.system('python generate_probabilities.py')