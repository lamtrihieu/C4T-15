# Part1

lap_quantity ={
    "HP":20,
    "Dell":50,
    "Macbook":12,
    "Asus":30,
}
print(lap_quantity)
print(lap_quantity["Macbook"])
input_lap = input("Choose a computer to check:")
if input_lap in lap_quantity:
    print("Compuer in dictionary,quantity:",lap_quantity[input_lap])
else:
    print("Computer not in dictionary")



# input_new_lap = input("New lap in dictionnary:")
# input_new_lap_quantity = int(input("New lap quantity:"))
# lap_quantity[input_new_lap]= input_new_lap_quantity

lap_quantity["Toshiba"]= 10
lap_quantity["Dell"]+= 10
lap_quantity["Macbook"] = 2
# for k,v in lap_quantity.items():
#     print(k,"-",v)

# Part3
# print("Macbook quantity=",lap_quantity["Macbook"])

lap_quantity["Fujitsu"] = 15
lap_quantity["Alienware"]= 5
# for k,v in lap_quantity.items():
#     print(k,"-",v)

# total_lap = sum(lap_quantity.values())
# print(total_lap)


# Part4
lap_price = {
    "HP":600,
    "Dell":650,
    "Macbook":12000,
    "Asus":400,
    "Toshiba":600,
    "Fujitsu":900,
    "Alienware":1000
}

# print(lap_price["Asus"])
# inpuy_lap2 = input("Name of lap to check price:")
# print (lap_price[inpuy_lap2])



# part5

# bill = lap_price["Asus"]*5

# print(bill)

# input_lap_bill = input("Lap to buy:")
# input_lap_bill_quantity = int(input("Quantity:"))
# if input_lap_bill in lap_price.keys():
#     if input_lap_bill_quantity <= lap_quantity[input_lap_bill]:   
#         print("Bill for lap:",lap_price[input_lap_bill]*input_lap_bill_quantity)
#         lap_quantity[input_lap_bill]+= -(input_lap_bill_quantity)
#         print("Remaining stock : ",lap_quantity[input_lap_bill])
#     else:
#         print("Lap not in stock")
# else:
#     print("Lap not in stock")

# print


# print(*lap_quantity.items(),sep=":")



# part6
# for q in lap_quantity and lap_price :
#     total_price = lap_price[q]*lap_quantity[q]
#     print(q,"has the total value of :","$",total_price)



