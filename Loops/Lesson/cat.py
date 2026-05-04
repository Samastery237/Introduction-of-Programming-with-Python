print("Meow")
print("Meow")
print("Meow")

# while coding

i = 1
while i <= 3:
    print("Meow")
    i = i + 1

i = 0
while i < 3:
    print("Meow")
    i = i + 1

i = 0
while i < 3:
    print("Meow")
    i += 1

# for coding

for i in (0, 1, 2):
    print("Meow")

for i in range(3):
    print("Meow")

for _ in range(3):
    print("Meow")

# shortcut fot loop

print("Meow\n" * 3, end="")

# counting how many meows

while True:
    n = int(input("What's n?: "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")

# using def with loop

def main():
    number = get_number()
    meow(3)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")