num_str = input("Give me a number: ")


if("." in num_str):
    locatedDot = num_str.find('.')
    print(int(num_str[:locatedDot]) + 1)
else:
    print(num_str)