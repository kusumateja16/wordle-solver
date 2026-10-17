from solver.feedback import get_feedback
from solver.candidates import filter_candidates
from solver.strategies import (
    rank_guesses_by_frequency,
    rank_by_information_gain,
)


def simulate_game(
    answer,
    word_list,
    max_guesses=6,
    strategy="frequency",
    allowed_guesses=None,
):
    answer = answer.upper()
    candidates = [word.upper() for word in word_list]

    guess_pool = [
        word.upper()
        for word in (
            allowed_guesses
            if allowed_guesses is not None
            else word_list
        )
    ]

    for attempt in range(1, max_guesses + 1):
        if not candidates:
            return {"solved": False, "guesses": attempt - 1}

        # If only one possible answer remains, guess it directly.
        if len(candidates) == 1:
            ranked = candidates
        elif strategy == "frequency":
            ranked = rank_guesses_by_frequency(guess_pool, candidates)
        elif strategy == "entropy":
            ranked = rank_by_information_gain(guess_pool, candidates)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        if not ranked:
            return {"solved": False, "guesses": attempt - 1}

        guess = ranked[0]
        feedback = get_feedback(answer, guess)

        if feedback == ["G"] * 5:
            return {"solved": True, "guesses": attempt}

        candidates = filter_candidates(candidates, guess, feedback)

    return {"solved": False, "guesses": max_guesses}
