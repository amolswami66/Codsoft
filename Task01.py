import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def on_task_type_change(event):
    task_type = task_type_combobox.get()
    if task_type == "Meeting" or task_type == "Event":
        date_entry_label.pack(pady=5)
        date_entry.pack(pady=5)
        time_entry_label.pack(pady=5)
        time_entry.pack(pady=5)
    elif task_type == "Birthday":
        date_entry_label.pack(pady=5)
        date_entry.pack(pady=5)
        time_entry_label.pack_forget()
        time_entry.pack_forget()
    else:
        date_entry_label.pack_forget()
        date_entry.pack_forget()
        time_entry_label.pack_forget()
        time_entry.pack_forget()

def add_task():
    task_type = task_type_combobox.get()
    task = task_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if task and task_type:
        if task_type == "Meeting" or task_type == "Event":
            if date and time:
                tasks_listbox.insert(tk.END, f"{task} ({task_type}) on {date} at {time}")
            else:
                messagebox.showwarning("Input Error", "Date and time are required for meetings and events.")
                return
        elif task_type == "Birthday":
            if date:
                tasks_listbox.insert(tk.END, f"{task} ({task_type}) on {date}")
            else:
                messagebox.showwarning("Input Error", "Date is required for birthdays.")
                return
        else:
            tasks_listbox.insert(tk.END, f"{task} ({task_type})")
        
        task_type_combobox.set("")
        task_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task type and name.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        updated_task_type = task_type_combobox.get()
        updated_task = task_entry.get()
        date = date_entry.get()
        time = time_entry.get()

        if updated_task and updated_task_type:
            if updated_task_type == "Meeting" or updated_task_type == "Event":
                if date and time:
                    tasks_listbox.delete(selected_task_index)
                    tasks_listbox.insert(selected_task_index, f"{updated_task} ({updated_task_type}) on {date} at {time}")
                else:
                    messagebox.showwarning("Input Error", "Date and time are required for meetings and events.")
                    return
            elif updated_task_type == "Birthday":
                if date:
                    tasks_listbox.delete(selected_task_index)
                    tasks_listbox.insert(selected_task_index, f"{updated_task} ({updated_task_type}) on {date}")
                else:
                    messagebox.showwarning("Input Error", "Date is required for birthdays.")
                    return
            else:
                tasks_listbox.delete(selected_task_index)
                tasks_listbox.insert(selected_task_index, f"{updated_task} ({updated_task_type})")
            
            task_type_combobox.set("")
            task_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task type and name.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Task type dropdown
task_type_label = tk.Label(root, text="Task Type:")
task_type_label.pack(pady=5)

task_type_combobox = ttk.Combobox(root, values=["Meeting", "Birthday", "Event"])
task_type_combobox.pack(pady=5)
task_type_combobox.bind("<<ComboboxSelected>>", on_task_type_change)

# Task entry
task_entry_label = tk.Label(root, text="Task:")
task_entry_label.pack(pady=5)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Date entry
date_entry_label = tk.Label(root, text="Date (DD-MM):")
date_entry = tk.Entry(root, width=40)

# Time entry
time_entry_label = tk.Label(root, text="Time (HH:MM):")
time_entry = tk.Entry(root, width=40)

# Buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

add_button = tk.Button(buttons_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(buttons_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(buttons_frame, text="Clear Tasks", command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5)

# Tasks listbox
tasks_listbox_label = tk.Label(root, text="Tasks:")
tasks_listbox_label.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack(pady=5)

# Run the application
root.mainloop()
