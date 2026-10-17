
import streamlit as st

from solver.dictionary import load_words
from solver.feedback import get_feedback
from solver.candidates import filter_candidates
from solver.strategies import (
    rank_guesses_by_frequency,
    rank_by_information_gain,
)

st.set_page_config(
    page_title="AI-Powered Wordle Solver",
    page_icon="🧩",
    layout="centered",
)

st.title("🧩 AI-Powered Wordle Solver")
st.write("Find possible Wordle answers using logic and information theory.")


@st.cache_data
def get_dictionaries():
    answers = [w.upper() for w in load_words("data/answers.txt")]
    allowed = [w.upper() for w in load_words("data/allowed_words.txt")]
    return answers, allowed


answers, allowed = get_dictionaries()

# Initialize game state
if "candidates" not in st.session_state:
    st.session_state.candidates = answers.copy()

if "history" not in st.session_state:
    st.session_state.history = []

if "solved" not in st.session_state:
    st.session_state.solved = False

if "answer" not in st.session_state:
    st.session_state.answer = ""


def reset_game():
    st.session_state.candidates = answers.copy()
    st.session_state.history = []
    st.session_state.solved = False
    st.session_state.answer = ""
    st.session_state.guess_input = ""


strategy = st.selectbox(
    "Choose strategy",
    ["Frequency", "Entropy"],
)

guess = st.text_input(
    "Enter your guess",
    max_chars=5,
    key="guess_input",
).strip().upper()

st.write("Feedback for each letter")

# Show the five letters and their feedback selectors
cols = st.columns(5)
feedback = ""

for i in range(5):
    letter = guess[i] if i < len(guess) else "-"

    with cols[i]:
        st.markdown(f"**{letter}**")

        color = st.selectbox(
            f"Tile {i + 1}",
            ["X", "Y", "G"],
            format_func=lambda x: {
                "X": "⬛ Gray",
                "Y": "🟨 Yellow",
                "G": "🟩 Green",
            }[x],
            key=f"tile_{i}",
        )
        feedback += color


# Submit a guess
if st.button("Submit guess", disabled=st.session_state.solved):
    if len(guess) != 5 or not guess.isalpha():
        st.error("Please enter a valid five-letter word.")

    elif guess not in allowed:
        st.error("That word is not in the allowed-word dictionary.")

    elif any(word == guess and result == feedback
             for word, result in st.session_state.history):
        st.warning("You already submitted this guess with the same feedback.")

    else:
        observed = list(feedback)

        new_candidates = filter_candidates(
            st.session_state.candidates,
            guess,
            observed,
        )

        if not new_candidates:
            st.error(
                "This feedback leaves no possible answers. "
                "Check the tile colors and try again."
            )
        else:
            st.session_state.history.append((guess, feedback))
            st.session_state.candidates = new_candidates

            if feedback == "GGGGG":
                st.session_state.solved = True
                st.session_state.answer = guess

            st.rerun()


# Reset button
st.button("Reset game", on_click=reset_game)


# Solved message
if st.session_state.solved:
    st.success(
        f"🎉 Puzzle solved! The answer is "
        f"{st.session_state.answer}."
    )


# Remaining answers
st.subheader("Remaining possible answers")

if st.session_state.candidates:
    st.write(
        f"**{len(st.session_state.candidates)}** candidates remain"
    )
    st.write(", ".join(st.session_state.candidates[:100]))
else:
    st.error(
        "No possible answers remain. Reset the game and check your feedback."
    )


# Recommended guesses
st.subheader("Recommended next guesses")

if st.session_state.solved:
    st.info("Puzzle completed! Reset to start a new game.")

elif st.session_state.candidates:
    if strategy == "Frequency":
        ranked = rank_guesses_by_frequency(
            allowed,
            st.session_state.candidates,
        )
    else:
        ranked = rank_by_information_gain(
            allowed,
            st.session_state.candidates,
        )

    st.write(
        ", ".join(ranked[:10]) if ranked else "No recommendations available."
    )

else:
    st.info("Reset the game or check your feedback to continue.")


# Guess history
st.subheader("Guess history")

if st.session_state.history:
    for word, result in st.session_state.history:
        tiles = " ".join(
            {
                "G": "🟩",
                "Y": "🟨",
                "X": "⬛",
            }[color]
            for color in result
        )
        st.write(f"**{word}** — {tiles}")
else:
    st.write("No guesses yet.")
