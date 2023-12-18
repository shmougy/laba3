def count_consonants(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for char in word.lower() if char in consonants)

def main():

    with open("F1.txt", "w") as f1:
        print("введите для ф1")
        while True:
            line = input()
            if not line:
                break
            f1.write(line + "\n")


    first_word = None
    with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
        for line in f1:
            words = line.strip().split()
            if first_word is None:
                first_word = words[0]
            if not any(word == first_word for word in words):
                f2.write(line)


    with open("F2.txt", "r") as f2:
        first_line = f2.readline().strip()
        consonant_count = count_consonants(first_line)

    print(f"согласные в ф2: {consonant_count}")

if __name__ == "__main__":
    main()
