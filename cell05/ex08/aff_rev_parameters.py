import sys

args = sys.argv[1:]

if(len(args) < 2):
    print("none")
else:
    for i in args[::-1]:
        print(i)

