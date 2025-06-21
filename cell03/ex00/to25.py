print("Enter a number less than 25")
number = int(input())

if(number < 25):
    for i in range(25 - number +1):
        print(f"Inside the loop, my variable is {number+i}")
else:
    print("Error")