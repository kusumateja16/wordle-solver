from collections import Counter


def rank_candidates(words):
    if not words:
        return []

    letter_counts = Counter(
        letter
        for word in words
        for letter in set(word.upper())
    )

    scores = {}

    for word in words:
        word = word.upper()
        scores[word] = sum(
            letter_counts[letter] for letter in set(word)
        )

    return sorted(scores, key=scores.get, reverse=True)
