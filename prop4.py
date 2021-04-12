# Problem 4
#-----------------
# The program takes a command line argument. This argument is the name of
# a text file. The program reads all the text, split them and calculate the 20
# Most used words in the file and then write them to a file called
# “popular_words.txt”.
# Implementation hint:
# my_str.split() #returns a List of my_str content by default separated by
# space.
# We can change the delimiter by passing it to split method
# Example:
# my_str.split(‘,’) #split by comma.

import sys
filename = sys.argv[1]
with open(filename,'r') as f:
    wordlist = f.read()
f.close()
wordlist = wordlist.split()

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


freqdict = wordListToFreqDict(wordlist)

sorteddict = sortFreqDict(freqdict) 

with open("popular_words.txt",'w') as f:
        f.write('(\'freq\', \'word\')')
        f.write('\n')
f.close()
most_used_words = sorteddict[0:20]
i = 0
for s in most_used_words:
    i += 1
    with open("popular_words.txt",'a') as f:
        f.write(str(i) + '.')
        f.write(str(s))
        f.write('\n')
    
f.close()