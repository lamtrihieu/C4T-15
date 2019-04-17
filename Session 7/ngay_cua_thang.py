month = int(input("Your month:"))

if 0<month <13:
    if month ==2:
        print("Your month has 28 days")
    elif month in [1,3,5,7.8,10,12]:
        print("Your month has 31 days")
    else:
        print ("your month has 30 days")
else:
    print("Invalid month")