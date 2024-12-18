#----------------->  1 . List ----------->


arrya_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arrya_list, "Print All List Elements") # print all elements


# Print Last Element of List
print(arrya_list[-1]) # Use of Slicing 

#print(arrya_list[start:end]) # Use of Slicing to print targeted elements resulst : 

#print first three elements of list print(arrya_list[:3]) here dont need to assign 0 . first element always from zero  

#print when need print 3 to all last  elements of list print(arrya_list[3:]) here dont need to assign last .  


# Max Min Sum

# sum of Max and Min elements

# -------------- 2 ----------------

lists = ['a', 'b', 'c', 'd', 'e', 'g']

for i in range(len(lists)):
    if lists[i] == 'a':
        print(f"find the index of element {lists[i]} at index {i}")
        break
else:
    print("element not found in the list")
        
# Using --------- enumerate()  methods ----------


