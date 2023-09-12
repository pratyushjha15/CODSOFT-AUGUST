import tkinter as tk
from tkinter import messagebox


# Function to evaluate and display the result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_window = tk.Toplevel(root)
        result_window.title("Result")

        result_label = tk.Label(result_window, text=f"Result: {result}")
        result_label.pack(padx=20, pady=20)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")


# Create the main application window
root = tk.Tk()
root.title("Scientific Calculator")

# Create and configure widgets
entry = tk.Entry(root, width=40)
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Pack widgets
entry.pack(padx=20, pady=20)
calculate_button.pack()

# Start the GUI main loop
root.mainloop()
