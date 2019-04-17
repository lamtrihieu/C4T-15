user = input ("Username:")
email = input("Email:")
pass_word = input("Password:")
re_password = input("Please reenter password:")

if user =="LamHieu":
    if "@gmail.com"  in email:
        if email == ("manemisgif@gmail.com"):
            if pass_word == re_password:
                if len(pass_word)>8:   
                    if pass_word == "121212121":
                        print ("Welcome LamHieu")
                    else:
                        print("Invalid password,please reenter")
                else:
                    print("Invalid password,please reenter")
            else:
                print("Different password,please reenter again")
        else:
             print("Wrong email,please reenter")
    else:
       print ("Invalid email,please reenter")
else:
    print("You are not LamHieu")       
