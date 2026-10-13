from solver.candidates import filter_candidates


def test_filter_candidates():
    words = ["APPLE", "AMPLE", "ALIEN", "ANGLE"]

    result = filter_candidates(
        words, "ALLEY", ["G", "Y", "X", "Y", "X"]
    )

    assert result == ["APPLE", "AMPLE", "ANGLE"]
