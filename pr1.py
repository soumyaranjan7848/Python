# find 2nd smallest number 
l=list(map(int,input().split()))
l=list(set(l))
l.sort()
print(l)
print("1st Smallest number is :",l[0])
print("2nd Smallest number is :",l[1])






