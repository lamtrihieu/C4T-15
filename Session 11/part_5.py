lap_quantity ={
    "HP":20,
    "Dell":50,
    "Macbook":12,
    "Asus":30,
}
# print(lap_quantity)
lap_quantity["Toshiba"]= 10
lap_quantity["Dell"]+= 10
lap_quantity["Macbook"] = 2
lap_price = {
    "HP":600,
    "Dell":650,
    "Macbook":12000,
    "Asus":400,
    "Toshiba":600,
    "Fujitsu":900,
    "Alienware":1000
}



bill = lap_price["Asus"]*5

print(bill)

input_lap_bill = input("Lap to buy:")
input_lap_bill_quantity = int(input("Quantity:"))
if input_lap_bill in lap_price.keys():
    if input_lap_bill_quantity <= lap_quantity[input_lap_bill]:   
        print("Bill for lap:",lap_price[input_lap_bill]*input_lap_bill_quantity)
        lap_quantity[input_lap_bill]+= -(input_lap_bill_quantity)
        print("Remaining stock : ",lap_quantity[input_lap_bill])
    else:
        print("Lap not in stock")
else:
    print("Lap not in stock")

print


print(*lap_quantity.items(),sep=":")