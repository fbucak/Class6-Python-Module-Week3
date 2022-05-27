# i. Write a function called int_return that takes an integer as input and returns the same integer.
# ii. Write a function called add that takes any number as its input and returns that sum with 2 added.
# iii. Write a function called greet that takes any name (string), and greets the person. E.g. “Hello Bob! Nice to meet you!” (Only returns the greeting string, printing is done in the main program.)
# iv. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
# v. Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
# vi. You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2.
# The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.


def int_return(x):
     return x

def add(x):
    return x+2

def greet(a):
    str="Hello "+a+"! Nice to meet you!"
    return str

def lenght(x):
    print("Longer than 5"if len(x)>=5 else"Less than 5")

def divider(x):
  return x/2

def sum(x):

  return divider(x)+6

def accum(x=[]):

   return sum(x)


lenght([1,2,3,4])