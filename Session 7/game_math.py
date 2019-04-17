from random import randint
while True:   
   
        n = randint(0,100)
        m = randint(0,100)
        r_ans =randint(0,200)
        ans = input("Answer:")


        print ((n+m),"=",r_ans)
        if (n+m)==r_ans:
            if ans == ("Y"):
                print("Correct")
            elif ans == ("N"):
                print ("Uncorrect")
        else:
            if ans == ("N"):
                print("Correct")
            elif ans == ("Y"):
                print ("Uncorrect")

    break