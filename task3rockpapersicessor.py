import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    if result == "Win":
        user_score += 1
        messagebox.showinfo("Result", f"You Win!\nYou: {user_choice}\nComputer: {computer_choice}")
    elif result == "Lose":
        computer_score += 1
        messagebox.showinfo("Result", f"You Lose!\nYou: {user_choice}\nComputer: {computer_choice}")
    else:
        messagebox.showinfo("Result", f"It's a Tie!\nYou: {user_choice}\nComputer: {computer_choice}")
    
    update_score()

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "Win"
    else:
        return "Lose"

def update_score():
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score()

# UI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")

tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", command=lambda: play_game("Rock")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Paper", command=lambda: play_game("Paper")).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Scissors", command=lambda: play_game("Scissors")).pack(side=tk.LEFT, padx=5)

score_label = tk.Label(root, text="User: 0  Computer: 0")
score_label.pack(pady=10)

tk.Button(root, text="Reset Scores", command=reset_game).pack(pady=5)

root.mainloop()
