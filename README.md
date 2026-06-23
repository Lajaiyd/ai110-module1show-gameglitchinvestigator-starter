# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Start the app with python -m streamlit run app.py. The game opens in the browser with a sidebar where the player can choose a difficulty level: Easy, Normal, or Hard. -->

2. <!-- Select a difficulty level and check the sidebar. The app shows the correct number range and the correct number of attempts allowed for that difficulty. -->

3. <!-- Enter a guess in the text box and click Submit Guess. If the guess is too high, the game now tells the player to go lower. If the guess is too low, the game now tells the player to go higher. -->

4. <!-- Continue guessing until the correct number is found or the attempt limit is reached. The attempts counter now starts at 0, so the player gets the full number of attempts shown in the sidebar. -->

5. <!-- If the player guesses correctly, the app shows a winning message with the secret number and final score. If the player runs out of attempts, the app shows a game-over message and reveals the secret number. -->

6. <!-- Click New Game to restart. The app now resets the attempts, score, status, history, and secret number, and the new secret number uses the correct range for the selected difficulty. -->
7. <!-- Run python -m pytest tests/test_game_logic.py to confirm the logic tests pass. The final test run showed that all 7 tests passed. -->
**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/


#================= 7 passed in 0.01s ==================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
