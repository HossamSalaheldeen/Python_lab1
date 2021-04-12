#3- Import operator module and explore its functions
#----------------------------------------------------
#Operator module
#Purpose:	Functional interface to built-in operators.
# Available In:	1.4 and later
from operator import *

print("Logical Operations")
a = -1
b = 5

print ('a =', a)
print ('b =', b)

print ('not_(a)     :', not_(a))
print ('truth(a)    :', truth(a))
print ('is_(a, b)   :', is_(a,b))
print ('is_not(a, b):', is_not(a,b))

print("Comparison Operators")

a = 1
b = 5.0
print

print ('a =', a)
print ('b =', b)
for func in (lt, le, eq, ne, ge, gt):
    print ('%s(a, b):' % func.__name__, func(a, b))

print("Arithmetic Operators")
a = -1
b = 5.0
c = 2
d = 6

print ('a =', a)
print ('b =', b)
print ('c =', c)
print ('d =', d)

print ('\nPositive/Negative:')
print ('abs(a):', abs(a))
print ('neg(a):', neg(a))
print ('neg(b):', neg(b))
print ('pos(a):', pos(a))
print ('pos(b):', pos(b))

print ('\nArithmetic:')
print ('add(a, b)     :', add(a, b))
print ('div(a, b)     :', floordiv(a, b))
print ('div(d, c)     :', truediv(d, c))
print ('floordiv(a, b):', floordiv(a, b))
print ('floordiv(d, c):', floordiv(d, c))
print ('mod(a, b)     :', mod(a, b))
print ('mul(a, b)     :', mul(a, b))
print ('pow(c, d)     :', pow(c, d))
print ('sub(b, a)     :', sub(b, a))
print ('truediv(a, b) :', truediv(a, b))
print ('truediv(d, c) :', truediv(d, c))

print ('\nBitwise:')
print ('and_(c, d)  :', and_(c, d))
print ('invert(c)   :', invert(c))
print ('lshift(c, d):', lshift(c, d))
print ('or_(c, d)   :', or_(c, d))
print ('rshift(d, c):', rshift(d, c))
print ('xor(c, d)   :', xor(c, d))