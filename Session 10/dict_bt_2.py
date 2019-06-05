skill1 ={
    "name":"Tackle",
    "level":1,
    "Damge":5,
    "Hit rate":0.3
}

skill2 = {
    "name":"Quick",
    "level":2,
    "Damge":3,
    "Hit rate":0.5
}
skill3 = {
    "name":"Strong",
    "level":3,
    "Damge":9,
    "Hit rate":0.2
}


list_skill = [skill1,skill2,skill3]
for i in list_skill:
    print(i["name"])
    print(i["level"])


level = int(input("Your level :"))
for i in list_skill:
    if level >= i["level"]:
        print("You can use skill :",i["name"]) 
    


