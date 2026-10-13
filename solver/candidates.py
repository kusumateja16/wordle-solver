from solver.feedback import get_feedback


def filter_candidates(words, guess, observed_feedback):
    remaining = []

    for word in words:
        result = get_feedback(word, guess)

        if result == observed_feedback:
            remaining.append(word)

    return remaining
