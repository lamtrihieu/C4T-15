lap ={
    "HP":20,
    "Pell":50,
    "Macbook":12,
    "Asus":30,
}
# print(lap)
# input_lap = input("Choose a computer:")
# if input_lap in lap:
#     print("Compuer in dictionary")
# else:
#     print("Computer not in dictionary")
# lap["Toshiba"]= 10
# lap["Pell"]+= 10
# lap["Macbook"] = "2"
# print(lap)




# sum_val = sum(lap.values())
# print (sum_val)



lap2 ={
    "HP":600,
    "Pell":650,
    "Macbook":12000,
    "Asus":900,
   

}
# price_pack = lap2["Asus"] * 5
# print (price_pack)
total_price_all = 0

for i in lap and lap2 :
    Total_price = (lap[i]) * (lap2[i])
    total_price_all += Total_price

    print(i,":",Total_price)

print("Total:",total_price_all) 



