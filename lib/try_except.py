def divide(num1, num2):
    try:
        quotient = num1/num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    
    except TypeError:
        print("Error: Input must be of type int or float")

    finally:
        print("Isn't division fun?")


divide(1,"Joel")