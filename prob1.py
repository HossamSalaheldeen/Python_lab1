# Problem 1
#--------------
# Given two points represented as x1,y1,x2,y2 .
# Return the (float) distance between them considering the following
# distance equation.
# Hint
# math.sqrt() could be a useful function.

import math
def hypotenuse(x1,y1,x2,y2):
    d=math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
    return d


print(hypotenuse(3,4,6,8))