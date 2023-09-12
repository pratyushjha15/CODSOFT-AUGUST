import tkinter as tk
import random
import string



def generate_password():
    length = int(length_entry.get())
    if length < 8:
        strength = "Weak"
    else:
        strength = "Strong"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    result_window = tk.Toplevel(root)
    result_window.title("Password Generator Result")

    password_label = tk.Label(result_window, text=f"Password: {password}")
    password_label.pack(padx=20, pady=10)

    strength_label = tk.Label(result_window, text=f"Strength: {strength}")
    strength_label.pack(padx=20, pady=10)



root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter the length of the password:")
length_entry = tk.Entry(root, width=10)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)


length_label.pack(padx=20, pady=10)
length_entry.pack(padx=20, pady=10)
generate_button.pack(pady=10)


root.mainloop()
