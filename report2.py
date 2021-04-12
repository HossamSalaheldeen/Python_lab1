#What are lambda functions in Python?

#In Python, an anonymous function is a function that is defined without a name.
#2- Lambda expression #Anonymous function
#---------------------------------------------
#While normal functions are defined using the def keyword in Python,
#anonymous functions are defined using the lambda keyword.
#Hence, anonymous functions are also called lambda functions.

#Syntax of Lambda Function in python
# lambda arguments: expression

#Examples of Lambda Function in python

#Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)