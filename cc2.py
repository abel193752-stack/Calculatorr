import tkinter as tk

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
                label_result.config(text="Error: Cannot divide by zero")
                return
            result = num1 / num2

        label_result.config(text=f"Result: {result}")

    except ValueError:
        label_result.config(text="Error: Enter valid numbers")

# Window
root = tk.Tk()
root.title("Calc")
root.geometry("300x250")

# Entry fields
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Buttons
tk.Button(root, text="Add", command=lambda: calculate("+")).pack(pady=2)
tk.Button(root, text="Subtract", command=lambda: calculate("-")).pack(pady=2)
tk.Button(root, text="Multiply", command=lambda: calculate("*")).pack(pady=2)
tk.Button(root, text="Divide", command=lambda: calculate("/")).pack(pady=2)

# Result
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

root.mainloop()


