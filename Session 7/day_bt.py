n = int(input("End here:"))




if n > 0:
    if n %2==0:
        for i in range (n+1,0,-2):
            print(i)
    else:
        for _ in range (n,0,-2):
            print(_)
else:
    pass