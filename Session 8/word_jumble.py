from random import choice,randint
words = ["boy","uoy","lop"]
random_word=words[randint(0,len(words))]
characters=list(random_word)
lst = []
loop = True
while loop:
    rand_character = choice(characters)
    characters.remove(rand_character)
    lst.append(rand_character)
    if len(characters)== 0:
        loop = False
print(*lst,sep="")
answer= input("Your answer:")
if answer == random_word:
    print ("correct")
else:
    print ("incorrect")

