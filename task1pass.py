import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Labels
tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

# Password Entry
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()