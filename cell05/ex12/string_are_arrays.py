import sys

args = sys.argv[1:]

count = 0

if(len(args) == 0):
    print("none")
else:
    for i in args[0]:
        if (i == "z"):
            count += 1

print(count * "z")