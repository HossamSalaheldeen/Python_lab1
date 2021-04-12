# 1- Python function enumerate()
#-------------------------------------
#What it does?
#enumerate(iterable, start=0)
#How it works
#The enumerate() method adds counter to an iterable and returns it (the enumerate object)
#You can convert enumerate objects to list and tuple using list() and tuple() method.

#example problem 6 again using enumerate
def find_all_indexes(str, ch):
    #make string as counter and value
    for i, ltr in enumerate(str):
        if ltr == ch:
            #return answer then again contiue the excution
            yield i


print(list(find_all_indexes("Google",'o')))