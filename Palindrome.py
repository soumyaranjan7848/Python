#******************1st************
def ispalindromeNumber(num):

    num_str=str(num)
    return num_str==num_str[::-1]

string_input='MAM'

print(ispalindromeNumber(string_input))

#****************2nd*************
str=input("Enter a string:")

if str==str[::-1]:
    print(str,"is palindrome")

else:
    print(str,"is not palindrome")

#****************3rd****************
    
txt=input("Enter a text: ")
rev_txt=""

for char in txt:
    rev_txt=char+rev_txt

if txt==rev_txt:
    print(txt,"is palindrome")

else:
    print(txt,"is not palindrome")

#*******************4th****************

def pal(number):
    print("original number is:", number)
    num_str = str(number)
    reversed_str = ""

    for char in num_str:
        reversed_str = char + reversed_str

    if num_str == reversed_str:
        print("number is palindrome")
    else:
        print("number is not palindrome")

pal(212)
