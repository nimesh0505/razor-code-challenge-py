# Razor Coding Test

### Welcome, and thank you for taking on this coding challenge! 🎉

This test is designed to assess your coding skills, problem-solving abilities, and familiarity with object-oriented programming. You’ll implement the logic for a simplified Blackjack game, complete with card counting.

We’ve provided the structure for the classes and tests—your task is to fill in the blanks and make everything work. Each part of the challenge gets progressively more complex, so take your time and have fun with it!

---

## 🃏 Introduction to Blackjack

Blackjack, also known as "21," is a popular card game where the goal is to get a hand value as close to 21 as possible without exceeding it (going "bust"). Players compete against the house (dealer), and each card has a point value:

- Number cards: face value (e.g., a 5 of Hearts is worth 5 points).
- Face cards (King, Queen, Jack): worth 10 points.
- Aces: worth either 1 or 11 points, depending on which is more beneficial for the hand.

**Card Counting** is a strategy to track high-value and low-value cards remaining in the deck, giving players an edge in predicting favorable situations.

---

## 💡 Challenge Overview

The challenge is divided into three exercises, each with increasing difficulty:

### 1. **Deck** (Basic)
You’ll create a class to represent a deck of cards. The deck should:
- Handle shuffling.
- Allow drawing cards.
- Reset to the original state.
*Hint: Focus on managing the cards and their order.*

### 2. **Blackjack Table** (Intermediate)
The table represents a game environment. You’ll:
- Manage multiple players and their hands.
- Implement core game mechanics like dealing, hitting, splitting, and folding.
*Hint: Think about how hands interact and how to ensure fairness for all players.*

### Bonus. **Game instance** (Advanced)
The game instance tracks the state of the deck and provides strategic advice. You’ll:
- Maintain a running count of cards dealt.
- Provide advice on what to do based on the count.
- Simulate the house’s hidden hand and implement a reveal mechanic.
*Hint: A good structure will make tracking the state much easier.*

---

## 🚀 Getting Started

1. **Fork the Repository**
   Start by forking the repository to your own GitHub account.
   Click the Fork button at the top right of the repository page.

2. **Clone the Repository**  
   Start by cloning this repository to your local machine:
   ```bash
   git clone <your-forked-repository-url>
   cd <repository-directory>
   ```

3. **Set Up Your Environment**  
   Ensure you have Python 3.7+ installed. Optionally, create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Explore the Codebase**
    Inside the project directory, you’ll find:
    - `deck.py`: Class skeleton for the Deck.
    - `blackjack.py`: Class skeleton for the Blackjack Table.
    - `game.py`: Class skeleton for the Counter.
    - `*_test.py`: Pre-written test cases for all classes.

5. **Run Tests**
    To check your progress, run the tests:
    ```bash
    python -m unittest discover .
    ```
    or alternatively:
    ```bash
    python test_all.py
    ```
    Tests will initially fail—your task is to make them pass!

---

## 📝 Submission Instructions

When you’ve completed the challenge:

1. **Commit Your Code**
    Ensure all your code changes are committed:
    ```bash
    git add .
    git commit -m "Completed the Blackjack Coding Test"
    ```

2. **Push to Your Repository**
    Push your code to your own GitHub repository:
    ```bash
    git push origin main
    ```

3. **Submit Your Work**
    Share the link to your repository with us. Please ensure your repository is public or grant access if it’s private.

---

## 🧐 Tips & Hints
- Start small! Each exercise builds on the previous one, so focus on completing the Deck class first.
- Write your own helper functions if they simplify the logic—modular code is easier to debug.
- Pay close attention to how the tests are structured—they often provide subtle hints about the expected behavior.

---

## 🌟 Good Luck!

We’re excited to see your approach to solving these challenges. Remember, there’s no single “right” way—feel free to showcase your style and creativity. If you have any questions, don’t hesitate to ask.

Happy coding! 🃏✨