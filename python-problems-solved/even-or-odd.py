

def check_even(n):

    if n % 2 == 0:
        return True
    else:
        return False

numbers = int(input(" X =  "))

checked = check_even(numbers)

if checked:
    print(f"{numbers} is an even number")
else:
    print(f"{numbers} is an Odd number")




