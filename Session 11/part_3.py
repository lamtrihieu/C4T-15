lap_quantity ={
    "HP":20,
    "Dell":50,
    "Macbook":12,
    "Asus":30,
}
# print(lap_quantity)

print("Macbook quantity=",lap_quantity["Macbook"])

lap_quantity["Fujitsu"] = 15
lap_quantity["Alienware"]= 5
for k,v in lap_quantity.items():
    print(k,"-",v)

total_lap = sum(lap_quantity.values())
print(total_lap)