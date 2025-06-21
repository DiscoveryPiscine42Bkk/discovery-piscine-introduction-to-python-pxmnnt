import sys

args = sys.argv[1:]

if (len(args) == 0):
    print("none")
else:
    for i in args:
        if(i[-3:] != "ism"):
            print(i + "ism")