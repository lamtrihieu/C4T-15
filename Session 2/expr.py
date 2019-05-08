from turtle import *
shape("turtle")
speed(-1)
n = int(input("start here:"))
m = int(input("stop here:"))
p = int(input("step here:"))
for i in range(n,m,p):
    for _ in range(i):
        forward(10)
        left(360/i)
mainloop()
# password = int(input("password:"))
# for password in ["1234"]:
#     print("Welcome")
