from functools import reduce
'''
Description: Fourth homework assignment
Written By: Avery Einhorn
Date: 11/6/2018
'''
'''
IMPORTANT:  The only function below that is allowed to use recursion is map2.
All other functions (including any helper functions you write) must not be recursive.  Instead, they should make calls to one or more of map, filter, and reduce to perform the necessary list traversals.
'''

def inRange(lo, hi, l):
    '''
    Returns all numbers in the list l that are between lo and hi (inclusive).
    '''
    loSort=list(filter(lambda x: x>=lo,l))
    hiSort=list(filter(lambda x: x<=hi,loSort))
    return hiSort
#print(inRange(5,15,[3,15,7,21,12,34]))

def zeroNegatives(l):
    '''
    Replaces all negative numbers in list l with 0,
    leaving all other numbers unchanged.
    '''
    return list(map(lambda x: x if (x>0) else 0,l))
#print(zeroNegatives([1,3,-4,-6,5,-5]))

def flatten(l):
    '''
    Flattens a list of lists into a single list.
    '''
    return list(reduce(lambda x1,x2: x1+x2, l))
#print(flatten([[1,2],[3],[],[4,5,6]]))

def halveEvens(l):
    '''
    Removes all odd integers from l and divides each even number in half.
    The list l is assumed to be a list of integers, and the function returns
    a list of integers.
    '''
    filteredList = list(filter(lambda x: x%2==0,l))
    return list(map(lambda x: int(x/2),filteredList))
#print(halveEvens([10,21,32,42,55]))

def map2(f, l1, l2):
    '''
    Behaves like the map function, but it traverses two lists simultaneously.
    Specifically, map(f, [x1,...,xn], [y1,...,yn]) returns [f(x1,y1), ..., f(xn,yn)].
    You may assume that l1 and l2 have the same length.
    '''
    if l1==[]:
        return []
    elif l1[1:]==[]:
        return list(map(f,l1,l2))
    return list(map(f,[l1[0]],[l2[0]]))+map2(f,l1[1:],l2[1:])
#print(map2(lambda x,y: [x,y], [1,2,3], [4,5,6]))

def dotProduct(v1,v2):
    '''
    Computes the dot product of the vectors v1 and v2, each of which is a list
    of numbers.  The dot product of [x1,...,xn] and [y1,...,yn] is
    x1*y1 + ... + xn*yn.
    You may assume that v1 and v2 have the same length.
    NOTE: You will want to make use of the map2 function that you defined above.
    '''
    return reduce(lambda x,y: x+y, map2(lambda x,y: x*y,v1,v2))
#print(dotProduct([1,2,3],[4,5,6]))