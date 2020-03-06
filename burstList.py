'''
Description: Project 6 Burst Zeros problem
Written By: Avery Einhorn
Date: 12/4/2018
'''
def findMin(l):
    if len(l)==1 or l==[]:
        return l
    else:
        if l[0]<l[1]:
            return findMin([l[0]]+l[2:])
        else:
            return findMin(l[1:])
def findMax(l):
    if len(l)==1 or l==[]:
        return l
    else:
        if l[0]>l[1]:
            return findMax([l[0]]+l[2:])
        else:
            return findMax(l[1:])

N=int(input("How long should the list of numbers be? "))
while N>25:
    N=int(input("Sorry that's too big. Try a number under 25: "))
l=[]
result=[]
for i in range(N):
    l+=[int(input("What number would you like to add to the list? "))]
#print("your list is "+str(l))
l+=[1]

def burstLength(lst):
    rslt=[]
    for i in range(len(lst)):
        if (l[i-1]!=0 or l[i-1]==None) and (l[i]==0):
            rslt=[1]+rslt
        elif l[i-1]==0 and l[i]==0:
            rslt[0]+=1
    suml=0
    if rslt==[]:
        print("You've got no zeroes!")
        return
    burstLengths=[]
    for i in rslt:
        suml+=i
        burstLengths=[i]+burstLengths
    avgl=suml/int(len(burstLengths))
    minl=findMin(burstLengths)[0]
    maxl=findMax(burstLengths)[0]
    print()
    print("Burst  Length")
    number=1
    for i in burstLengths:
        print("  "+str(number)+"      "+str(i))
        number+=1
    print("Average burst length: "+str(avgl))
    print("Minimum burst length: "+str(minl))
    print("Maximum burst length: "+str(maxl))
    print("Total number of zeroes: "+str(suml))
    return 
burstLength(l)