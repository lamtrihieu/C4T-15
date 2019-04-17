while True:
    usr = input("Password:")
    le = int(len(usr))
    if usr.isdigit():
        if le>=8:
            print("Welcome")
            break    
        else:
            print("invalid") 
    else:
        print("invalid") 