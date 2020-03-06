'''
Description: homework three file
Written By: Avery Einhorn
Date: 11/2/18
'''
def partition(v, l): #always returns two lists, a list of all v's in l, and a list of everything else in l
    # SOLUTION: return [[x for x in l if x==v],[x for x in l if x!=v]]
    if l==[]:
        return [[],[]] 
    else:
        tail=partition(v,l[1:]) #will always be two lists
        head=l[0] #defines head in base case and all recursive cases
        if head==v: #in any subcase as well
            return [[head]+tail[0],tail[1]] #puts the recursively found values that are equal to v in first box as well as the value that we are examining right now. Everything else goes in second box
        else:
            return [tail[0],[head]+tail[1]] #obvs put recursively found v's in box one, everything else goes in box two including our current value
#print(partition(2,[2,1,3,5,2,-5,222,22,2]))

def countDistinct(l): # can only use partition
    if l==[]:
        return 0
    else:
        return 1+countDistinct(partition(l[0],l)[1])
#print(countDistinct([1,2,3,4,5,4,3,2,1,22,3]))

def selectionSort(l):
    if l==[]:
        return l
    else: 
        return partition(min(l),l)[0]+selectionSort(partition(min(l),l)[1])
#print(selectionSort([6,4,3,5,3,68,2,325,2,4]))


# for use in mergesort below; do not edit
def merge(l1, l2): # only works if argument lists are presorted, so need l of incoming lists to be 1 or otherwise sorted lists!!!
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])

def mergeSort(l): #can only use merge and len functions
    if len(l)<=1: #base case returns a "sorted" list of one item
        return l
    else:
        halfList=int(len(l)/2) # determines the length of our broken up lists
        first = l[halfList:]
        rest = l[:halfList]
        return merge(mergeSort(first),mergeSort(rest)) #merges two lists, our broken up lists, which at their base case will be "sorted" as single-item lists
#print(mergeSort([3093,49429,393,29,39,-3,-314,93]))