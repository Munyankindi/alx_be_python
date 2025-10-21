def safe_divide():
    try:
        numerator = float(input("enter the numerator: "))
        denominator = float(input("enter the denominator: "))
        division = numerator / denominator
        print (division)
    except ZeroDivisionError:
        print("Error: You cannot divide by Zero")
    except ValueError:
        print("Error:Please Enter Valid number")
        
safe_divide()