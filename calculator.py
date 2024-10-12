while True:
    s1 = float(input("First number: "))
    s2 = float(input("Second number: "))

    op = input("Choose an operator: ")

    if op=='+':
        print(s1+s2)
    elif op == '-':
        print(s1 + s2)
    if op == '*':
        print(s1 + s2)
    elif op == '/':
        if s2 != 0:
            print(s1 + s2)
        else:
            print("Error")
    else:
        print("Error")