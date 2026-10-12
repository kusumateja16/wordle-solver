import streamlit as st

st.set_page_config(
    page_title="AI Wordle Solver",
    page_icon="🧩",
    layout="wide"
)

st.title("🧩 AI-Powered Wordle Solver")
st.subheader("Solve smarter. Guess better.")

st.write(
    "An intelligent Wordle assistant using logic, "
    "pattern matching, and information theory."
)

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Word Length", "5 letters")
col2.metric("Maximum Guesses", "6")
col3.metric("AI Strategy", "Coming soon")

st.info(
    "Welcome! Your AI solver is under development. "
    "The next step is building its word-filtering engine."
)

st.markdown("### Project roadmap")
st.write("1. Word feedback and candidate filtering")
st.write("2. Intelligent guess recommendations")
st.write("3. Entropy and probability analysis")
st.write("4. Automated performance evaluation")
