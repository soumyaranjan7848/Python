# 1) Given a two list of numbers,write a program to create a new list 
#such that the,new list should contain odd numbers from the first list 
#and even numbers from the second list.Solu:-

def merge_list(list1, list2):
    result_list = []
    
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [1, 9, 2, 0, 5]
list2 = [7, 4, 6, 5, 6]
print("result list:", merge_list(list1, list2))
