def factorial():
    n=int(input("enter your number:"))
    
    if n<0:
        print("factorial of negative numbers is not possible")
    elif n ==0:
        print(1, "factorial of 0 is 1" )
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i

    print(factorial)     





factorial()        

        