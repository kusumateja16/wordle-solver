from solver.simulator import simulate_game


def test_simulator_solves_single_word():
    result = simulate_game("APPLE", ["APPLE"])

    assert result["solved"] is True
    assert result["guesses"] == 1


def test_simulator_stops_when_candidates_are_empty():
    result = simulate_game("APPLE", ["CRANE", "SLATE"], max_guesses=2)

    assert result["solved"] is False
    assert result["guesses"] == 1
