list_highscore = [45,56,67,78]
index_i = 0

loop = True

while loop:
    print(list_highscore)
    new_high = int(input("New highscore:"))
    list_highscore.append(new_high)
    list_highscore.sort(reverse=True)
    index_i+=1
    if index_i == 1:
        # loop = False  
        for i in range(len(list_highscore)):      
            print(i+1, ":", list_highscore[i])
        break

    
    