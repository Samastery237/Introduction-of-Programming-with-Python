import random

cards = ["Jack", "Queen", "King"]

def main():
    random.seed(0)
    print(random.choices(cards, k=2))

main()
