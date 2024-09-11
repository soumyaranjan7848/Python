# 1)  Write a function to return True if the first and last number of a given list is same. 
#     If numbers are different then return False.

def fir_lst_samenum(numList):
    print("Given list:",numList)

    FirstElement=numList[0]
    LastElement=numList[-1]
    if (FirstElement==LastElement):
        return True

    else:
        return False

list1=[10,20,4,2,3,4,10]
print("Result is :",fir_lst_samenum(list1))

list2=[4,4,5,6,7,8,2,3,9]
print("Result is :",fir_lst_samenum(list2))


# 2) Iterate the given list of numbers and print only those numbers which are divisible by 5

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')

for num in num_list:
    if num % 5 == 0:
        print(num)


#3) Return the count of a given substring from a string.
#Or
#   Write a program to find how many times substring appears in the given string.

str = "Soumya is a good boy.Soumya is a good sportsman"
cnt = str.count("Soumya")
print("Substrings:",cnt)


#4) print the partten in increasing order.

for num in range(10):
    for i in range(num):
        print (num, end=" ") 
    print("\n")

#5) Write a program to check if the given number is a palindrome number.

def pal(num):
    print("original number is:",num)
    num_str=str(num)
    rev=""

    for char in num_str:
        rev=char+rev

    if num_str==rev:
        print("number is paliandrom")
    
    else:
        print("number is not paliandrom")

pal(212)

