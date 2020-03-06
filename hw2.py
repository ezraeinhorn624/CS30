from doctest import testmod
'''
Description: CS30 Homework 2
Written By: Avery Einhorn
Date: 10/14/18
'''
def doubleAll(l):
    """Returns a list that is identical to l but with each value doubled.
    Arguments:
    l -- a list of integers"""
    if l==[]:
        return []
    else:
        return [2*l[0]]+doubleAll(l[1:])
print (doubleAll([1,-2,4]))

def countPos(l):
    """Returns the number of elements in l that are positive.
    Arguments:
    l -- a list of integers    """
    if l==[]:
        return 0
    elif (l[0]) > 0:
        return 1+countPos(l[1:])
    else:
        return countPos(l[1:])
print(countPos([-1,0,4,-2,6]))
    
def intRange(low, high):
    """Returns a list of integers in the range low to high, inclusive.
    Arguments:
    low -- the lower bound (an integer)
    high -- the upper bound (an integer)    """
    if low>high:
        return []
    else:
        return [low]+intRange(low+1,high)
print(intRange(1,9))

def merge(l1, l2):
    """Merge two sorted integer lists to produce a new sorted list of their elements.
    Arguments:
    l1 -- the first list
    l2 -- the second list    """
    if l1==[] and l2!=[]:
        return l2
    elif l2==[] and l1!=[]:
        return l1
    elif l1==[] and l2==[]:
        return []
    elif l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:],l2)
    elif l2[0] < l1[0]:
        return [l2[0]] + merge(l1,l2[1:])
    elif l1[0] == l2[0]:
        return [l1[0]]+[l2[0]]+merge(l1[1:],l2[1:])
print(merge([1,2,3,7,9],[3,7,7,8,9]))

# run all doctests whenever this file is run (via the Run menu in IDLE)
if __name__ == '__main__':
    testmod()