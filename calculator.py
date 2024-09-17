def calculator():
  """A simple calculator with basic arithmetic operations."""

  print("Welcome to the Simple Calculator!")

  while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division(/)")
    print("5. Quit")

    choice = int(input("Enteryour choice (1-5): "))

    if choice == 1:
      sum = num1 + num2
      print("Result:", sum)
    elif choice == 2:
      sub = num1 - num2
      print("Result:", sub)
    elif choice == 3:
      mul = num1 * num2
      print("Result:",mul)
    elif choice == 4:
      if num2 == 0:
        print("Error: Division by zero is not allowed.")
      else:
        div = num1 / num2
        print("Result:",div) 

    elif choice == 5:
      print("Exiting the calculator.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  calculator()