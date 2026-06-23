# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Hint should guide player | Hint was incorrect(said Go Lower instead of higher) | 

New game should start with a clean slate| New game button didnt reset the game | Game over. Start a new game to try again.

Developer debug should be visible to developer only| Developer debug showing on player end | 

Number of attempts should match number of times advertised | Player number of attempts is lower than as advertised | Out of Attempts

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude Code as my AI teammate while working through the debugging process. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). One correct suggestion was to inspect the hint logic inside check_guess, because the messages for “Too High” and “Too Low” were swapped. I verified that fix manually by testing guesses above and below the secret number and checking whether the message pointed in the correct direction.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). One misleading issue I had to catch was that the original tests expected check_guess to return only a string, but the app actually needed the function to return both an outcome and a hint message, so I updated the tests to match the real function behavior.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I decided a bug was really fixed only when I could reproduce the original problem and then confirm that the corrected behavior matched what the game should do. For example, I added pytest cases that specifically checked the backwards hint bug: a guess that is too high must include “LOWER” in the hint, and a guess that is too low must include “HIGHER.” I also added a test for the integer-secret comparison and a test for the difficulty ranges, because the new-game reset bug involved using a hardcoded range instead of the selected difficulty range. After fixing the test mismatch and adding the bug-targeting tests, I ran python -m pytest tests/test_game_logic.py, and all 7 tests passed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

Some bugs were easier to test with pytest than others. The hint logic, integer comparison, and difficulty range logic were good unit-test targets because they lived in logic_utils.py. The attempts counter, debug panel, and full “New Game” reset were more tied to Streamlit session state and UI behavior, so I verified those manually in the app instead of trying to force them into pure unit tests

- Did AI help you design or understand any tests? How?
AI helped me think through which parts belonged in unit tests and which parts needed manual Streamlit testing.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I learned that Streamlit reruns the script from top to bottom whenever the user interacts with the page, such as clicking a button or submitting a guess. Because of that, important values like the secret number, attempts, score, status, and guess history need to be stored in st.session_state. I would explain session state to a friend as Streamlit’s memory for one user’s current session. Without session state, the app can forget values or reset parts of the game at the wrong time.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to reuse in future labs is writing tests that directly target the bugs I fixed, not just general tests that check the happy path. In this project, the original tests only checked the outcome labels, but the actual backwards-hint bug was in the message text, so the better tests had to assert on the hint direction too.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time I work with AI on a coding task, I would ask it to explain the function contract clearly before accepting or editing tests.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I noticed that code can look reasonable while still hiding logic bugs, state bugs, and test assumptions that need human verification.
