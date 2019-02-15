
wordstring ='rudra and divya are kids'
wordstring +=' rudra is a boy and divya is a girl '
wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
print("list\n"+str(wordlist)+"\n")

from collections import Counter
list1=wordlist
counts = Counter(list1)
print(counts)


# new programme
from collections import Counter
list1=['apple','egg','apple','banana','egg','apple']
counts = Counter(list1)
print(counts)
# output like this Counter({'apple': 3, 'egg': 2, 'banana': 1})