import tkinter as tk
from tkinter import messagebox

def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("300x250")

# Entry fields
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Buttons
tk.Button(root, text="Add", width=10, command=lambda: calculate("+")).pack(pady=2)
tk.Button(root, text="Subtract", width=10, command=lambda: calculate("-")).pack(pady=2)
tk.Button(root, text="Multiply", width=10, command=lambda: calculate("*")).pack(pady=2)
tk.Button(root, text="Divide", width=10, command=lambda: calculate("/")).pack(pady=2)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()