import sys

args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    count = 0
    words_arr = args[1].split(" ")
    if(args[0] in words_arr):
        for i in words_arr:
            if i == args[0]:
                count += 1

    if(count == 0):
        print("none")
    else:
        print(count)



