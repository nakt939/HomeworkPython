while True:
    n = int(input("Write a number: "))
    if n == 0:
        break
    for i in range(1,10,1):
        for j in range(1, n+1, 1):
            print(f"{j} * {i} = {i*j}", end='\t')
        print()