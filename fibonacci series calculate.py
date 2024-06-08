def Fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1   
    else:
        for i in range(2,n+1):
            c = a+b
            a = b
            b = c
            print(c)


print(Fibonacci(9))