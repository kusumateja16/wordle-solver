import sys
from pathlib import Path
from statistics import mean
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solver.dictionary import load_words
from solver.simulator import simulate_game


def evaluate(answers, allowed_words, strategy):
    results = []
    start = perf_counter()

    for answer in answers:
        results.append(
            simulate_game(
                answer,
                answers,
                max_guesses=6,
                strategy=strategy,
                allowed_guesses=allowed_words,
            )
        )

    elapsed = perf_counter() - start
    solved = [r for r in results if r["solved"]]

    return {
        "total": len(results),
        "solved": len(solved),
        "failed": len(results) - len(solved),
        "rate": 100 * len(solved) / len(results) if results else 0,
        "average": mean(r["guesses"] for r in solved) if solved else 0,
        "runtime": elapsed,
    }


answers = load_words("data/answers.txt")
allowed_words = load_words("data/allowed_words.txt")

for strategy in ("frequency", "entropy"):
    result = evaluate(answers, allowed_words, strategy)

    print(f"\nStrategy: {strategy}")
    print(f"Answers tested: {result['total']}")
    print(f"Solved: {result['solved']}")
    print(f"Failed: {result['failed']}")
    print(f"Solve rate: {result['rate']:.1f}%")
    print(f"Average guesses (solved only): {result['average']:.2f}")
    print(f"Runtime: {result['runtime']:.4f} seconds")
