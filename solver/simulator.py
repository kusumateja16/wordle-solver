from solver.feedback import get_feedback
from solver.candidates import filter_candidates
from solver.strategies import rank_candidates


def simulate_game(answer, word_list, max_guesses=6):
    answer = answer.upper()
    candidates = [w.upper() for w in word_list]

    for attempt in range(1, max_guesses + 1):
        if not candidates:
            return {"solved": False, "guesses": attempt - 1}

        guess = rank_candidates(candidates)[0]
        feedback = get_feedback(answer, guess)

        if guess == answer:
            return {"solved": True, "guesses": attempt}

        candidates = filter_candidates(candidates, guess, feedback)

    return {"solved": False, "guesses": max_guesses}
