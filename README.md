# 🎰 LuckyDraw

**LuckyDraw** is a simple terminal-based Python slot machine game. Players deposit money, choose how many lines to bet on, and spin to generate a 3x3 grid of random symbols. Matching symbols on a line wins you a payout based on symbol value!

## 📦 Features

- Deposit system and balance tracking
- Randomized 3x3 slot machine spin
- Adjustable line betting (up to 3 lines)
- Symbol-based rewards (A, B, C, D) with custom values
- Payout based on symbol value and bet amount
- Simple terminal UI
  
## 🧠 Symbol Details

| Symbol | Count | Value |
|--------|-------|--------|
| A      | 2     | 5x     |
| B      | 4     | 4x     |
| C      | 6     | 3x     |
| D      | 8     | 2x     |

> A match of the same symbol on a horizontal line results in a win.

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Run the script:

```bash
python lucky_draw.py
💰 Example Gameplay

What would you like to deposit? $100
Enter the number of lines to bet on (1-3)? 2
What would you like to bet on each line? $10
You're betting amount $10 on 2 lines. Total bet is $20.

A | C | B
A | C | D
D | D | D

You won $20.
You won on lines: 3
```
## 🖥️ GUI Version (Tkinter)
A GUI version of LuckyDraw is now available!

- 🎨 User-friendly interface built with Tkinter
- 🔢 Supports 1 to 5 betting lines
- 🎰 5x3 spinning slot grid with styled layout
- 💸 Displays winnings and remaining balance
- 🖱️ Interactive inputs and spin button

### ▶️ To Run the GUI:
> python lucky_draw_gui.py
