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
            result = num1 / num2

        label_result.config(text=f"Result: {result}")

# Window
root = tk.Tk()
root.title("calc")
root.geometry("300x250")

# Buttons
tkinter.Button(root, text="Add", calculate("+")).pack(pady=2)
tkinter.Button(root, text="Subtract", calculate("-")).pack(pady=2)
tkinter.Button(root, text="Multiply", calculate("*")).pack(pady=2)
tkinter.Button(root, text="Divide", calculate("/")).pack(pady=2)

# Result
label_result = tk.Label(root, text="Result: ")

root.mainloop()

