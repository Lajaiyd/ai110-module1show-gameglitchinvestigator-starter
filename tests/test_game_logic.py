from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting the specific bugs we fixed ---

def test_too_high_hint_says_go_lower():
    # BUG: hints were backwards. A guess that is too high must tell the
    # player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()

def test_too_low_hint_says_go_higher():
    # BUG: hints were backwards. A guess that is too low must tell the
    # player to go HIGHER, not lower.
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()

def test_check_guess_handles_integer_secret():
    # BUG: on some attempts the secret was passed as a string, which broke
    # the numeric comparison. With an int secret, a correct guess wins.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_difficulty_ranges_are_correct():
    # BUG: "New Game" used a hardcoded 1-100 range instead of the range for
    # the selected difficulty. Each difficulty must report its own range.
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
