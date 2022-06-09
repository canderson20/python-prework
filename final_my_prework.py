# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 

def hello_name(user_name):
    """Greet the user of the program."""
    print("Hello, " + user_name.title() + "!")

hello_name("Colton")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing. 

def first_odds():
    """Display every odd number from 1-100."""
even_numbers = []
odd_numbers = []

for number in range(1,101):
    if number % 2==0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    
print(odd_numbers)


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been definted as below. 

def max_num_in_a_list(a_list):
    """Present the max number from the list."""
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max
a_list = [1,2,3,4,5,6,7,8,9,20]
print(max(a_list))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Present if the input year is a leap year."""
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return True
    else:
        return False

year = int(input())
print(is_leap_year(year))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """Determine if numbers in the list are consecutive or not."""
    
    if len(a_list) < 1:
        return False
    min_val = min(a_list)
    max_val = max(a_list)
    if max_val - min_val + 1 == len(a_list):
        for i in range(len(a_list)):
            if a_list[i] < 0:
                j = -a_list[i] - min_val
            else:
                j = a_list[i] - min_val
            if a_list[j] > 0:
                a_list[j] = -a_list[j]
            else:
                return False
        return True
    return False
a_list = [2,3,4,5,6,7]
b_list = [1,2,4,5]
print(is_consecutive(a_list))
print(is_consecutive(b_list))

