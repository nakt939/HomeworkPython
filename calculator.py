print("CALCULINA")

o = input("Введите операцию: +, -, *, /: ")

f = float(input())
s = float(input())

if(o == "+"):
    print(f+s)
elif(o == "-"):
    print(f-s)
elif(o == "/"):
    print(f/s)
elif(o == "*"):
    print(f*s)
else:
    print("Ошибка!")