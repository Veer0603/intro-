import math 
def sin(x,terms):
    value = 0
    for n in range(terms):
        value += (-1)**n * (x**(2*n+1))/math.factorial(2*n+1)
    return value
a = float(input("ENTER THE VALUE OF DEGREE IN RADIANS : "))
b = int(input("ENTER THE NUMBER OF TERMS OF APPROXIMATION : "))    
approx_sin = sin(a,b)
print("sin(",a,")=",approx_sin)