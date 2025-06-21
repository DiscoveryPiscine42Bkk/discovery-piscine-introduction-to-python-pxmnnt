age = int(input("Please tell me your age: "))

print(f"You are currently {age} years old.")

for i in range(3):
    print(f"In {(i+1)*10} years, you will be {age + ((i+1)*10)} years old.")