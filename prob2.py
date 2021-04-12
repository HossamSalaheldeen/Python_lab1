# Problem 2
#---------------
# Given a list of numbers, create a function that returns a list where all similar
# elements have been reduced to a single element.
# So [1, 2, 2, 3, 2] returns [1, 2, 3]

def remove_dublicates(li):
    unique_list = list(dict.fromkeys(li))
    return unique_list



print(remove_dublicates([1,2,2,3,2]))
