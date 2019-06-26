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

print(lap_price["Asus"])
inpuy_lap2 = input("Name of lap to check price:")
print (lap_price[inpuy_lap2])