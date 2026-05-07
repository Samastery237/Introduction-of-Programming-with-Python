import sys

if len(sys.argv) < 2:
    print("Too Few Arguments")
elif len (sys.argv) > 2:
    print("Too Manyy Arguments")
else:
    print("Hello, my name is", sys.argv[1])