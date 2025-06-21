
firstTime = True

while(True):
    if(firstTime):
        first_time_input = input("What you gotta say?: ")
        firstTime = False
    else:
        repeated_input = input("I got that! Anything else? : ")
        if(repeated_input == "STOP"):
            break

    
