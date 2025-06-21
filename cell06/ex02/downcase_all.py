import sys

def downcase_it(string):
    return string.lower()

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for i in args:
        print(downcase_it(i))