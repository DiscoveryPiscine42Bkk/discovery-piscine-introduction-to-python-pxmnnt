import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    str_length = len(string)

    while str_length < 8:
        string += "Z"
        str_length = len(string)


    print(string)

args = sys.argv[1:]

if len(args) < 1:
    print("none")
else:
    for i in args:
        if len(i) > 8:
            shrink(i)
        else:
            enlarge(i)