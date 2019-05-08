from random import randint
# score0 = 0
# score1 = 0
# score2 = 0
# score3 = 0

# print ("""Decide whether these calculations are correct or not
#                            choose N or Y                       """)

# # while True:
#         current_score = score0 + score1+ score2 +score3+1
#         n = randint(0,10)
#         m = randint(0,10)
#         ans_p = (n+m)
#         ans_n = (n-m)
#         r_ans_p = ans_p + randint(1,8)
#         r_ans_n = ans_n - randint(1,8)
#         rng = randint(0,4)


#         if rng ==0:
#             print  (n,"+",m,"=",ans_p,"?")
#             ans = input ("Answer:")
#             if ans == ("Y"):
#                 print ("Correct answer")
#                 score0+= 1
#                 print  ("current score:",current_score)
#             elif ans == ("N"):
#                 print ("Uncorrect answer")
#                 print ("Final score :",current_score-1)
#                 break
#             else:
#                 break
#         if rng == 1:
#             print (n,"-",m,"=",ans_n,"?")
#             ans = input ("Answer:")
#             if ans ==("Y"):
#                 print ("Correct answer")
#                 score1+= 1
#                 print  ("current score:",current_score)
#             elif ans ==("N"):
#                 print ("Uncorrect answer")
#                 print ("Final score :",current_score-1)
#                 break
#             else:
#                 break
#         if rng == 2:
#             print (n,"+",m,"=",r_ans_p,"?")
#             ans = input ("Answer:")
#             if ans == ("N"):
#                 print ("Correct answer")
#                 score2+= 1
#                 print  ("current score:",current_score)

#             elif ans ==("Y"):
#                 print ("Uncorrect answer")
#                 print ("Final score :",current_score-1)
#                 break
#             else:
#                 break
#         if rng == 3:
#             print (n,"-",m,"=",r_ans_n,"?")
#             ans = input ("Answer:")
#             if ans == ("N"):
#                 print ("Correct answer")
#                 score3+= 1
#                 print  ("current score:",current_score)

#             elif ans ==("Y"):
#                 print ("Uncorrect answer")
#                 print ("Final score :",current_score-1)
#                 break
#             else:
#                 break
score = 0
while True:
    a = randint(0, 10)
    b = randint(0, 10)

    c = randint(-2, 2)
    print(a, "+", b, "=", a+b+c)
    answer = input("Enter your answer: ")
    if c == 0:
        if answer == "Y" or answer == "y":
            print("Correct!")
            score += 1
            print("Your Score: ", score)
        elif answer == "N" or answer == "n":
            print("Incorrect!")
            break
        else:
            print("Your Score: ", score)
            break
    else:
        if answer == "Y" or answer == "y":
            print("Incorrect!")
            print("Your Score: ", score)
            break
        elif answer == "N" or answer == "n":
            print("Correct!")
            score += 1
            print("Your Score: ", score)
        else:
            break
