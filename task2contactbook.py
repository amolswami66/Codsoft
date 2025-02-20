import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter Contact Name:")
    if name:
        contacts[name] = {}
        messagebox.showinfo("Success", "Contact Added Successfully")
    else:
        messagebox.showerror("Error", "Name is required!")

def search_contact():
    query = simpledialog.askstring("Search", "Enter Name:")
    contact_list.delete(0, tk.END)
    for name in contacts.keys():
        if query in name:
            contact_list.insert(tk.END, name)

def delete_contact():
    name = simpledialog.askstring("Delete", "Enter Contact Name to Delete:")
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact Deleted Successfully")
    else:
        messagebox.showerror("Error", "Contact Not Found")

# UI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=10)

contact_list = tk.Listbox(frame, width=50, height=10)
contact_list.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

root.mainloop()
