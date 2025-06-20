import random
import tkinter as tk
from tkinter import messagebox, ttk

# Constants
MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1
ROWS = 5
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # Check symbol in the first column of each row
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

class SlotMachineApp:
    def __init__(self, master):
        self.master = master
        master.title("🎰 Slot Machine Game")
        master.geometry("440x580")
        master.configure(bg="#2c3e50")

        self.balance = 0

        title = tk.Label(master, text="Slot Machine", font=("Helvetica", 20, "bold"), fg="white", bg="#2c3e50")
        title.pack(pady=10)

        self.balance_label = tk.Label(master, text="Balance: $0", font=("Arial", 14), fg="white", bg="#2c3e50")
        self.balance_label.pack(pady=5)

        self.deposit_frame = tk.Frame(master, bg="#2c3e50")
        self.deposit_frame.pack(pady=2)
        self.deposit_entry = ttk.Entry(self.deposit_frame, width=15)
        self.deposit_entry.pack(side=tk.LEFT, padx=5)
        self.deposit_button = ttk.Button(self.deposit_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side=tk.LEFT)

        self.input_frame = tk.Frame(master, bg="#2c3e50")
        self.input_frame.pack(pady=5)
        self.lines_label = tk.Label(self.input_frame, text=f"Lines (1-{MAX_LINES}):", bg="#2c3e50", fg="white")
        self.lines_label.grid(row=0, column=0, padx=5)
        self.lines_entry = ttk.Entry(self.input_frame, width=10)
        self.lines_entry.grid(row=0, column=1, padx=5)

        self.bet_label = tk.Label(self.input_frame, text="Bet/Line:", bg="#2c3e50", fg="white")
        self.bet_label.grid(row=1, column=0, padx=5)
        self.bet_entry = ttk.Entry(self.input_frame, width=10)
        self.bet_entry.grid(row=1, column=1, padx=5)

        self.spin_button = ttk.Button(master, text="🎲 Spin", command=self.spin)
        self.spin_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Arial", 12), fg="#f1c40f", bg="#2c3e50")
        self.result_label.pack(pady=10)

        self.slot_display = tk.Text(master, height=ROWS, width=30, state="disabled", font=("Courier", 14), bg="#34495e", fg="white", relief="flat")
        self.slot_display.pack(pady=10)

    def deposit(self):
        try:
            amount = int(self.deposit_entry.get())
            if amount > 0:
                self.balance += amount
                self.update_balance()
                self.deposit_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Deposit must be more than 0.")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def spin(self):
        try:
            lines = int(self.lines_entry.get())
            if not (1 <= lines <= MAX_LINES):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", f"Enter lines between 1 and {MAX_LINES}.")
            return

        try:
            bet = int(self.bet_entry.get())
            if not (MIN_BET <= bet <= MAX_BET):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
            return

        total_bet = lines * bet
        if total_bet > self.balance:
            messagebox.showerror("Error", f"Not enough balance. Current: ${self.balance}")
            return

        self.balance -= total_bet
        slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
        self.display_slots(slots)

        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        self.balance += winnings
        self.update_balance()

        self.lines_entry.delete(0, tk.END)
        self.bet_entry.delete(0, tk.END)

        if winnings > 0:
            self.result_label.config(
                text=f"🎉 You won ${winnings} on line(s): {', '.join(map(str, winning_lines))}!"
            )
        else:
            self.result_label.config(text="😢 No winnings this time. Try again!")

    def display_slots(self, slots):
        self.slot_display.config(state="normal")
        self.slot_display.delete("1.0", tk.END)
        for row in range(ROWS):
            row_symbols = [col[row] for col in slots]
            self.slot_display.insert(tk.END, " | ".join(row_symbols) + "\n")
        self.slot_display.config(state="disabled")

if __name__ == '__main__':
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
