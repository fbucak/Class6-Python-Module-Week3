# 4. QUESTION 4
# i. Write a recursive function sum_of_numbers to calculate the sum of numbers within a given range that takes start and end as parameters. The function should work whether start is less or greater than end.
# ii. Write a function called input_function to ask the user to enter the starting and ending numbers and call sum_of_numbers with those arguments and prints the result.
# iii. Write the same function sum_of_numbers to calculate the sum of numbers but this time it takes a list of integers as an argument and calculates the sum of the integers in the list. Invoke the function in the main program.a
# def input_function():
#    start,end=[int(input("Please enter a number")) for _ in range(2)]
#    if start>end:
#        return end,start
#    else:
#        return start, end
# def sum_of_numbers():
#      numbers=input_function()
#      return sum(range(numbers[0],numbers[1]+1))
#
# print(sum_of_numbers())

def sum_of_numbers():
     return sum(input_function())

def input_function():
    my_list=[int(input()) for _ in range(int(input("please enter the number of list elements ")))]
    return my_list
print(sum_of_numbers())