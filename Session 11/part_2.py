lap_quantity ={
    "HP":20,
    "Dell":50,
    "Macbook":12,
    "Asus":30,
}
# print(lap_quantity)
input_new_lap = input("New lap in dictionnary:")
input_new_lap_quantity = int(input("New lap quantity:"))
lap_quantity[input_new_lap]= input_new_lap_quantity

lap_quantity["Toshiba"]= 10
lap_quantity["Dell"]+= 10
lap_quantity["Macbook"] = 2
for k,v in lap_quantity.items():
    print(k,"-",v)