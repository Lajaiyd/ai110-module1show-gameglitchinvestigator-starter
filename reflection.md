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
| | | | |Hint should guide player | Hint was incorrect(said Go Lower instead of higher) | 
| | | | | New game should start with a clean slate| New game button didnt reset the game | Game over. Start a new game to try again.
| | | | | Developer debug should be visible to developer only| Developer debug showing on player end | 
          Number of attempts should match number of times advertised | Player number of attempts is lower than as advertised | Out of Attempts

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude Code as my AI teammate while working through the debugging process. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). One correct suggestion was to inspect the hint logic inside check_guess, because the messages for “Too High” and “Too Low” were swapped. I verified that fix manually by testing guesses above and below the secret number and checking whether the message pointed in the correct direction.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). One misleading part of the AI-generated code was the way it handled the secret number as a string on even attempts; instead of solving the comparison problem cleanly, it created a type bug that made the game harder to reason about.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Ran Strea
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
