
from random import choice
input_=input("You word here:")
words = list(input_)
loop = True
lst=[]

while loop:
    random_word = choice(words)
    words.remove(random_word)
    lst.append(random_word)
    if len(words)== 0:
        loop = False
print(*lst,sep="\n")






