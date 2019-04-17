from turtle import  *

shape("turtle")
speed(-1)




# for i in range(30):
#         for n in range (4):
#                 forward(100)
#                 right(90)
#         left (30)

for i in range (1,300):
        for n in range(4):
                forward(100)
                right(90)
        left(360/i)


mainloop()