#**************************##***********************
        
def fizzbuzz(n):
    if n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    elif n%3==0 and n%5==0:
        return "fizzbuzz"
    else:
        return n
print(fizzbuzz(15))


#***************************#****************
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("fizzbuzz",end=" ")
    elif i%3==0:
        print("fizz",end=" ")
    elif i%5==0:
        print("buzz",end=" ")
    else:
        print(i,end=" ")

