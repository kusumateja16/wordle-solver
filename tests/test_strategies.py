from solver.strategies import rank_candidates


def test_rank_candidates():
    ranked = rank_candidates(["APPLE", "AMPLE", "ALIEN"])

    assert len(ranked) == 3
    assert set(ranked) == {"APPLE", "AMPLE", "ALIEN"}


def test_empty_candidates():
    assert rank_candidates([]) == []

from solver.strategies import calculate_entropy


def test_entropy_empty_answers():
    assert calculate_entropy("APPLE", []) == 0.0


def test_entropy_is_nonnegative():
    answers = ["APPLE", "AMPLE", "ALIEN", "ANGLE"]
    assert calculate_entropy("APPLE", answers) >= 0.0
