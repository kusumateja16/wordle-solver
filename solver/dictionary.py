from pathlib import Path


def load_words(filename):
    path = Path(filename)

    words = set()

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().upper()

            if len(word) == 5 and word.isalpha():
                words.add(word)

    return sorted(words)
