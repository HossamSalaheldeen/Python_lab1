# Problem 6
#-----------------
# The program takes a string and a character and returns a list with all the
# locations that character was found in the given string.
# Implementation hint:
# String “Google” char ‘o’
# Outoupt: [1,2]

def loc_of_char(s,c):
    lst = []
    for i in range(len(s)):
        if (s[i] == c):
            lst.append(i)       
    return lst

print(loc_of_char("Google",'o'))