from solver.feedback import get_feedback

def test_correct_word():
    assert get_feedback("APPLE", "APPLE") == ["G"] * 5

def test_repeated_letters():
    assert get_feedback("APPLE", "ALLEY") == ["G", "Y", "X", "Y", "X"]

def test_invalid_length():
    try:
        get_feedback("APP", "APPLE")
        assert False, "Expected ValueError"
    except ValueError:
        pass
