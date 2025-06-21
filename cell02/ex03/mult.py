print("Enter the first number:")
first_number = int(input())

print("Enter the second number:")
second_number = int(input())

answer = first_number * second_number

print(f"{first_number} x {second_number} = {answer}")

if(answer == 0):
    print("This result is both positive and negative.")
elif(answer > 0):
    print("This result is positive.")
elif(answer< 0):
    print("This result is negative.")