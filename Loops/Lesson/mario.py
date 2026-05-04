# manual

print("#")
print("#")
print("#")

# for loop

for _ in range(3):
    print("#")

# loop with def

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")


main()

def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")


main()

# now in row brick

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# now in square brick

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

def print_row(width):
    print("#" * width)

    
main()