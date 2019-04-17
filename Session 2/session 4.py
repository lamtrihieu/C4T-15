t_m = int(input("current month:"))
print ("Current season:")

# if t_m in range (1,13):
if  t_m in range(1,4):
        print ("Xuan")
elif  t_m in range (5,8):
        print ("He")
elif  t_m in range (9,11):
        print ("Thu")
elif  t_m in range (10,13):
        print ("Dong")
else:
    print ("time invalid")
