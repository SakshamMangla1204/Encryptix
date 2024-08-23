import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters
    if 'digits' in complexity:
        characters += string.digits
    if 'special' in complexity:
        characters += string.punctuation
    if not characters:
        raise ValueError("No character sets specified.")
    return ''.join(random.choice(characters) for _ in range(length))

def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        complexity = complexity_var.get().split()
        password = generate_password(length, complexity)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Label(root, text="Complexity (e.g., 'letters digits special'):").pack(pady=5)
complexity_var = tk.StringVar()
complexity_entry = tk.Entry(root, textvariable=complexity_var)
complexity_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password:")
result_label.pack(pady=5)

root.mainloop()
