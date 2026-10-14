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
import math
from collections import Counter
from solver.feedback import get_feedback


def calculate_entropy(guess, possible_answers):
    if not possible_answers:
        return 0.0

    patterns = Counter(
        tuple(get_feedback(answer, guess))
        for answer in possible_answers
    )

    total = len(possible_answers)
    entropy = 0.0

    for count in patterns.values():
        probability = count / total
        entropy -= probability * math.log2(probability)

    return entropy


def rank_by_information_gain(guesses, possible_answers):
    return sorted(
        guesses,
        key=lambda guess: calculate_entropy(guess, possible_answers),
        reverse=True
    )
