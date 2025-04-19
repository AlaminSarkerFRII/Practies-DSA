


array_list = [0, 1, 2, 3, 4, 5, 6, 7,500]

#  Method 1
print(max(array_list), "Max value") # Max value of list
print(min(array_list), "Min value") # Min value of list


#  Method 2
# Find Max number of elements

max_value = array_list[0] # let first index of element is max value

for value in array_list:
    if value > max_value:
        print(value, max_value, "value" , "max value")
        max_value = value
        
    
    
print("Max value ", max_value)

# Find Min number of elements

min_value = array_list[0] # let first index of element is min value

for value in array_list:
    if value < min_value:
        min_value = value
        
    
    
print("min_value ", min_value)
        

        
    