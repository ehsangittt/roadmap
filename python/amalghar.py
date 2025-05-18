def calc(a, b, op):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "%":
        print(a % b)
    else:
        print("ERROR")

a = int(input("A? "))
b = int(input("B? "))
op = input("Amalgar? (+, -, *, %): ")

calc(a, b, op)
