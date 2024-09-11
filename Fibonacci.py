n=int(input("Enter length of Fibonacci Sequence:"))

n1=0
n2=1
count=2

if n<0:
    print("Enter onlt +ve Values")
elif n==1:
    print(n1)
else:
    print(n1)
    print(n2)
    while count<n:
        n3=n1+n2
        print(n3)
        count+=1
        n1=n2
        n2=n3

#*******************###********************
        
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(Fibonacci(n-1)+Fibonacci(n-2))
    
n=int(input("Enter a number:"))
print("Fibonacci series:")
for n in range(0,n):
    print(Fibonacci(n))

#**********************right or wronge*******************

n=int(input("Enter a number:"))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y