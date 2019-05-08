
list_=["1","2","3","4"]
while True:
    
    input_ =input("Choose your command:")
    if input_=="c"or input_=="C":
        new_item =input("What would you like to add to your list?:")
        list_.append(new_item)
        print (list_)
    if input_=="r"or input_=="R":
        
        if int(len(list_))==0:
            print("This list has no item")
        else:   
            print (list_)
    if input_=="u" or input_=="U":
        update_index=int(input("At which index would you want to change?:"))
        updated_index=input("What would you want to change it to?:")
        list_[update_index]=updated_index
        print(list_)
    if input_=="d" or input_=="D":
        delete_index=int(input("At which index would you want to delete?:"))
        list_.pop(delete_index)
        print(list_)
        break









            