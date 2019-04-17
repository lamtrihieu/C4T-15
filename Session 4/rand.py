user = input ("Username:")
pass_word = input("Password:")

if user =="techkids":
    if pass_word == "codethechange":
        print ("Welcome,superuser")
    else:
        print("Invalid password")
else:
    print("You are not superuser")       
