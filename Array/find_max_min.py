


array_list = [0, 1, 2, 3, 4, 5, 6, 7,500]

# Find Max number of elements

max_value = array_list[0] # let first index of element is max value

for value in array_list:
    #print(value)
    #print(max_value)
    if value > max_value:
        max_value = value
        
    
    
print("Max value ", max_value)

# Find Min number of elements

min_value = array_list[0] # let first index of element is min value

for value in array_list:
    #print(value)
    #print(min_value)
    if value < min_value:
        min_value = value
        
    
    
print("min_value ", min_value)
        

        
    