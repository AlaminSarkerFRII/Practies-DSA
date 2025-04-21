# Return Second-Largest Element in an Array

# 1.Sort the array in descending order and return the second element.
# 2. Use a set to remove duplicates and then sort the array in descending order.

def second_largest(arr):
    arr.sort(reverse=True)
    # remove duplicates
    # create a dictionary from the list with unique value and then convert it back to a list
    # This method is generally faster than the loop method for larger lists.
    arr = list(dict.fromkeys(arr))
    if len(arr) < 2:
        return -1
    return arr[1]

# Example usage
array = [10, 20, 4, 45, 99, 99]
print(second_largest(array)) # Output: 45




# ===== Find Third-Largest Element in an Array



def find_third_largest(arr):
    arr.sort(reverse=True)

    arr_sorted_desc = list(dict.fromkeys(arr))

    if len(arr_sorted_desc) < 3:
        return -1

    return arr_sorted_desc[2]



