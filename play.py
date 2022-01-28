
import pickle
import re

wordle = pickle.load( open( "wordle.p", "rb" ) )


notinword = ''
inword = [''] * 5
wordmatch = '•••••'


def printWordle(wordle, n):
    n = min(len(wordle), n)
    if not n:
        print('\n\nNo words left in dictionary\n\n')
    for i in range(0,n):
        print('%i\t%s\t%f' % (i+1, wordle[i]['word'], wordle[i]['prob']))
    
    if n < len(wordle):
        print('•••')

def cutWordle(wordle, current):
    newwordle = []
    for i, word in enumerate(wordle):
        keepword = True
        searchword = word['word']
        
        if searchword == current:
            keepword = False
            continue
        
        for c in ''.join(inword):
            if not c in searchword:
                keepword = False
        
        newsearchword = ''
        for j in range(0,5):
            if not wordmatch[j] == '•':
                if not searchword[j] == wordmatch[j]:
                    keepword = False
                    newsearchword += '.'
                else:
                    newsearchword += '·'
            else:
                newsearchword += searchword[j]
        searchword = newsearchword
        
        for c in notinword:
            if c in searchword:
                keepword = False
        
        for j in range(0,5):
            for c in inword[j]:
                if searchword[j] == c:
                    keepword = False
        
        if keepword:
            newwordle.append(word) 
    
    return newwordle

for mainloop in range(1,7):
    print('\n\nTry #%i' % mainloop)
    n = 5
    printWordle(wordle, n)

    while True:
        current = input('Current try (enter for first in list, "more" for more matches): ')
        
        if not current:
            current = wordle[0]['word']
        if current == 'more' or current == 'm':
            n += 5
            printWordle(wordle, n)
        number = True
        for c in current:
            if not c in '0123456789':
                number = False
        if number:
            current = wordle[int(current)-1]['word']
        if len(current) == 5:
            break
    
    print('Input: ' + current)


    while True:
        result = input('Wordle response (x for black, y for yellow, g for green): ')
        if not result:
            result = 'ggggg'
        if result == 'x':
            result = 'xxxxx'
        if len(result) == 5:
            break
    
    if result == 'ggggg':
        print('\n\nDONE!!!\n\n')
        break
    
    newwordmatch = ''
    for i in range(0,5):
        if result[i] == 'x':
            if not current[i] in notinword:
                notinword += current[i]
        if result[i] == 'y':
            if not current[i] in inword[i]:
                inword[i] += current[i]
        if result[i] == 'g':
            newwordmatch += current[i]
        else:
            newwordmatch += wordmatch[i]
    
    for c in inword:
        notinword = re.sub(c, '', notinword)
    
    wordmatch = newwordmatch

    # print(notinword)
    # print(inword)
    # print(wordmatch)
    
    wordle = cutWordle(wordle, current)
    
    if not len(wordle):
        break




















