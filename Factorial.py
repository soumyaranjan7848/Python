#**********************************using Recursion calling a function under the another function***
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n*factorial(n-1))
print(factorial(4))
    
#************************