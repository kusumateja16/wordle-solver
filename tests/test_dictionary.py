from solver.dictionary import load_words


def test_load_words(tmp_path):
    file = tmp_path / "words.txt"
    file.write_text("apple\nAPPLE\ncat\ncrane1\nample\n")

    result = load_words(file)

    assert result == ["AMPLE", "APPLE"]
