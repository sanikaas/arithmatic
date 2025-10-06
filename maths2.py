def mult(a, b):
    return a * b

def div(a, b):
    return a / b

if _name_ == "_main_":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("multiplication:", mult(x, y))
    print("division:", div(x, y))