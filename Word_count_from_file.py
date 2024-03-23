def count_word(filename):
    word_counts = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

        for word, num in word_counts.items():
            print(f"{word} -> {num}")


count_word("word.txt")
