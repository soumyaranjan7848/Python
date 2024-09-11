# 1)  Given two integer numbers return their product only,
#     if the product is equal to or lower than 1000, else return their sum.

def multi_or_sum (num1,num2):
    input=num1,num2
    prod= num1*num2

    if prod <=1000:
        return prod

    else:
        return num1+num2

res=multi_or_sum(num1=20,num2=30)
print("The Result is", res)

res=multi_or_sum(num1=30,num2=40)
print("The Result is", res)

# 2)  Write a program to iterate the first 10 numbers and in each iteration,
#     print the sum of the current and previous number.

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0
for i in range(1, 11):
    sum = previous_num + i
    print("Current Number: ", i, "Previous Number: ", previous_num, " Sum: ", sum)
    previous_num = i

# 3)  Write a program to accept a string from the user and display, 
#     characters that are present at an even index number.

#                                              **************** first approch ****************
word = input('Enter word ')
print("Original String:", word)

size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])

#                                                 ****************  2nd approch ***************
word = input('Enter word ')
print("Original String:", word)
#using list slicing = convert string to list
x = list(word)
for i in x[0::2]:
    print(i)


# 4) Write a program to remove characters from a string starting,
#    from zero up to n and return a new string.

str = input('Enter string')
print("You entered string is: ",str)
l = list(str)
for i in l[4:]:
    print(i)