# Problem 3
#-------------
# Consider dividing a string into two halves.
# Case 1:
# The length is even, the front and back halves are the same length.
# Case 2:
# The length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form :
# (a-front + b-front) + (a-back + b-back)

def combine_strs(a,b):
    print(len(a))
    a_front = a[0:len(a)//2 if len(a)%2 == 0 else ((len(a)//2)+1)]
    print(a_front)
    a_back = a[((len(a)//2)) if len(a)%2 == 0 else ((len(a)//2)+1):len(a)]
    print(a_back)
    print(len(b))
    b_front = b[0:len(b)//2 if len(b)%2 == 0 else ((len(b)//2)+1)]
    print(b_front)
    b_back = b[((len(b)//2)) if len(b)%2 == 0 else ((len(b)//2)+1):len(b)]
    print(b_back)
    ab = (a_front + b_front) + (a_back + b_back)
    return ab

print(combine_strs("abcd","abcd"))
