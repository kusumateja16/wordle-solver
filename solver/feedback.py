def get_feedback(answer, guess):
    answer = answer.upper()
    guess = guess.upper()

    if len(answer) != 5 or len(guess) != 5:
        raise ValueError("Both words must contain 5 letters")

    feedback = ["X"] * 5
    remaining = list(answer)

    # First pass: find green letters
    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = "G"
            remaining[i] = None

    # Second pass: find yellow letters
    for i in range(5):
        if feedback[i] != "G" and guess[i] in remaining:
            feedback[i] = "Y"
            remaining[remaining.index(guess[i])] = None

    return feedback
