print("--- Welcome to My First Calculator ---")

# We start a loop that runs as long as 'True' is true (which is forever!)
while True:
    num1 = float(input("\nEnter first number: "))
    op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    
    # Check if the user wants to stop
    if op.lower() == 'q':
        print("Goodbye!")
        break  # This 'breaks' the loop and ends the program
        
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/":
        # Pro tip: Check if they are trying to divide by zero!
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid operator!")
