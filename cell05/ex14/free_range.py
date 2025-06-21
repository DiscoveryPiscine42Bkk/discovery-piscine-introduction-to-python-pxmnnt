import sys

args = sys.argv[1:]

if(len(args) == 0 or len(args) > 2):
    print("none")
else:
    first_number, second_number = args
    print(list(range(int(first_number), int(second_number) + 1)))