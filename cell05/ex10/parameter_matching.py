import sys

if (len(sys.argv) != 2):
    print("none")
else:
    expected = sys.argv[1]
    actual = input("What was the parameter? ")
    if(expected == actual):
        print("Good job!")
    else:
        print("Nope, sorry...")