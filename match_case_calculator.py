num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
operation = input("choose the operation: (+,-,*,/)")
match operation:
    case "+":
        print("result is ", num1 + num2)
    case "-":
        print("result is ", num1 - num2)
    case "*":
        print("result is ", num1 * num2)
    case "/":
        if num2 == 0:
            print("cannot divide by Zero")
        else:
            print("result is ", num1/num2)

