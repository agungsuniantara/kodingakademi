for i in range(4): # i = 1
    for z in range(5): # z = 0
        print("*", end = "")
    print("")


for i in range(4): # i = 0
    for z in range(5): # z = 0
        if z <= i:
            print("*", end = "")
    print("")
        
        