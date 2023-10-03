import tkinter as tk
import secrets
import string
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    
    if length < 4:
        messagebox.showerror("Invalid Length", "Password length should be at least 4 characters.")
        return
    
    password_strength = strength_var.get()
    
    if password_strength == "Weak":
        characters = string.ascii_lowercase
    elif password_strength == "Medium":
        characters = string.ascii_letters + string.digits
    elif password_strength == "Strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("250x250")


length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

strength_label = tk.Label(root, text="Select Password Strength:")
strength_label.pack()

strength_var = tk.StringVar()
strength_var.set("Medium")  # Default strength

strength_weak = tk.Radiobutton(root, text="Weak", variable=strength_var, value="Weak")
strength_medium = tk.Radiobutton(root, text="Medium", variable=strength_var, value="Medium")
strength_strong = tk.Radiobutton(root, text="Strong", variable=strength_var, value="Strong")

strength_weak.pack()
strength_medium.pack()
strength_strong.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root)
password_entry.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

root.mainloop()
