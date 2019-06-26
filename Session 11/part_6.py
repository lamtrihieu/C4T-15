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
for q in lap_quantity and lap_price :
    total_price = lap_price[q]*lap_quantity[q]
    print(q,"has the total value of :","$",total_price)