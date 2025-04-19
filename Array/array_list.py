#----------------->  1 . List ----------->


arrya_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(arrya_list, "Print All List Elements") # print all elements


# Print Last Element of List
# print(arrya_list[-1]) # Use of Slicing

#print(arrya_list[start:end]) # Use of Slicing to print targeted elements resulst : 

#print first three elements of list print(arrya_list[:3]) here dont need to assign 0 . first element always from zero  

#print when need print 3 to all last  elements of list print(arrya_list[3:]) here dont need to assign last .  

# -------------- 2 ----------------

"""
- enumerate() function adds a counter to each item in a list or other iterable. 
- It turns the iterable into something we can loop through,
- where each item comes with its number (starting from 0 by default)
"""


def find_element(lists, target):
    for index, item in enumerate(lists):
        if item == target:
            print(f"find the index of element {item} at index {index}")
            print(f"the length of the list is {len(lists)}")
            break
    else:
        print("element not found in the list")
        
# Using --------- enumerate()  methods ----------

target = 'g'
list_items = ['a', 'b', 'c', 'd', 'e', 'g']

print(find_element(list_items, target))