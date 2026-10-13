from solver.strategies import rank_candidates


def test_rank_candidates():
    ranked = rank_candidates(["APPLE", "AMPLE", "ALIEN"])

    assert len(ranked) == 3
    assert set(ranked) == {"APPLE", "AMPLE", "ALIEN"}


def test_empty_candidates():
    assert rank_candidates([]) == []
