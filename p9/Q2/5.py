def q5():    
    def power(a, b):
        if b == 0:
            return 1
        return a * power(a, b - 1)
    a = int(input("Enter the base : "))
    b = int(input("Enter the exponent : "))
    print("The ans is :",power(a,b))
q5()