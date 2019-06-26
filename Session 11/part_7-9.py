from random import randint

main_chracter = {
    "Name":"Light",
    "Age":17,
    "Strength":8,
    "Defense":10,
    "HP":100,
    "Backpack":["Shield","Breadloaf"],
    "Gold":100,
    "Level":2,
}
# part7
main_chracter["Gold"]+= 50

main_chracter["Backpack"].append("Flint Stone")

main_chracter["Pocket"] = ["Monster Dex","Flashlight"]
# part8
skill1 ={
    "Name":"Tackle",
    "Minimum level":1,
    "Damage":5,
    "Hit rate":0.3
}

skill2 = {
    "Name":"Quick attack",
    "Minimum level":2,
    "Damage":3,
    "Hit rate":0.5
}
skill3 = {
    "Name":"Strong Kick",
    "Minimum level":3,
    "Damage":9,
    "Hit rate":0.2
}
skills = [skill1,skill2,skill3]

# for i in range(len(skills)):
#     for k,v in skills[i].items():
#         if k == "Name":
#             print(i+1)
#         print(k,":",v)

combat = True
while combat:
    print("Your skills are:")
    for i in range(len(skills)):
        for k,v in skills[i].items():
            if k == "Name":
                print(i+1)
            print(k,":",v)
    hit_rng = randint(0,1)
    
    
    
    skill_choice = int(input("Please choose a skill's number to use:"))
    if main_chracter["Level"] >= skills[skill_choice-1]["Minimum level"]:
        print("Skill usable")
        
        if hit_rng > skills[skill_choice-1]["Hit rate"]:
            print("Inflicted damage:",skills[skill_choice-1]["Damage"])
            combat =False
        else:
            print("Attack missed")
            print("YOU DIED")
            combat = False
    else:
        print("Skill not usable")
        print("YOU DIED")
        break
















