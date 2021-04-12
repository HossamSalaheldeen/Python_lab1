# Problem 5
#------------
# The program takes a string and remove the vowels character from it then
# print its new version
# Implementation hint:
# So, “Mobile” becomes “Mbl”

def remove_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for c in s.lower():
        if c in vowels:
            s = s.replace(c,"")

    return s


print(remove_vowels("Mobile"))