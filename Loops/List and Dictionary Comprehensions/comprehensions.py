# Version 1

def get_words(filename):
    with open(filename) as file:
        return file.read().split()

def save_counts(counts):
   for word, count in counts.items():
        print(f"{word}: {count}", end="")
        print()

def main():
    counts = {}
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 2]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1  # Fixed: Use [] instead of ()
        else:
            counts[word] = 1
    
    save_counts(counts)

main()