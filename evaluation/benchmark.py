import sys
from pathlib import Path
from statistics import mean

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solver.dictionary import load_words
from solver.simulator import simulate_game

answers = load_words("data/answers.txt")

results = [
    simulate_game(answer, answers)
    for answer in answers
]

solved = [r for r in results if r["solved"]]
failed = len(results) - len(solved)

print("Total answers tested:", len(results))
print("Solved:", len(solved))
print("Failed:", failed)
print(f"Solve rate: {len(solved) / len(results) * 100:.1f}%")

if solved:
    print(f"Average guesses among solved games: {mean(r['guesses'] for r in solved):.2f}")
