from random import randint,choice

words = ["boy","girl","car"]
rng=randint(0,len(words)-1)
rand_word=words[rng]
lst=[]
loop = True
while loop:
    rand_character=choice(rand_word)
    rand_word.remove(rand_character)
    lst.append(rand_character)
    if len(rand_word)== 0:
        loop =False
    print(lst)
    answer = input("Answer:")
    if answer == rand_word:
        print ("correct")
    else:

        print("incorrect")







    













