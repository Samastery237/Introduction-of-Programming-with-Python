name = []

for _ in range(3):
    name.append(input("What's your name? "))

for name in sorted(name):
    print(f"hello, {name}")


# open formula

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# getting the existing file to read file

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# Arrangement mode / sorting time

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# reverse mode

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
