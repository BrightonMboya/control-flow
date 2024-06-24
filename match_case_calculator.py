while (True):
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case operation if operation == "+":
            print(f"The Result is {firstNumber + secondNumber}")
        case operation if operation == "-":
              print(f"The Result is {firstNumber - secondNumber}")
        case operation if operation == "*":
              print(f"The Result is {firstNumber * secondNumber}")
        case operation if operation == "/":
              if secondNumber == "0":
                  print("Cannot divide by zero")
                  break
              else:
                print(f"The Result is {firstNumber / secondNumber}")
    break