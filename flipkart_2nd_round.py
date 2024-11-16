"""

A pizza shop offers three pizza sizes- small , medium and large. The pizza shop has one delivery van with a capacity K.
A small pizza occupies 1 capacity, a medium pizza occupies 2 capacity, and a large pizza occupies 3 capacity.
The pizza shop has to deliver the orders that it receives in order, and the delivery van has enough fuel for T trips.
Determine the minimum value of K such that all the orders can be delivered within T trips.

Example:
Order:
[[1,2,1],[0,2,1],[4,0,1]]
T = 2
Order 1: 1 small, 2 medium, 1 large –4
Order 2: 0 small, 2 medium, 1 large –3
Order 3: 4 small, 0 medium, 1 large –5  

1, 4, 3
0 ,4, 3
4, 0, 3

"""


def asd(arr, max_trip):
    ar = []
    for obj in arr:
        ar.append(obj[0]*1+ obj[1]*2 + obj[2]*3)
    
    total_cap = sum(ar)
    
    for cap in range(max(ar), sum(ar)+1):
        t = 0
        stack = []
        total = total_cap

        for obj in ar:
            if sum(stack)+obj<cap:
                stack.append(obj)
            elif sum(stack)+obj==cap:
                t+=1
                stack = []
            else:
                t+=1
                stack = [obj]
    
        if stack:
            t+=1

        if t==max_trip:
            return cap
    
    return "no solution"

    




print(asd([[1,2,1],[0,2,1],[4,0,1]], 2))



"""

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.
 
Example 1:
Input: s = "bcabc"
Output: "abc"

b[0]
c[1]
a[2]
b[3]
c[4]
bca
cab --c


Example 2:
Input: s = "cbacdcbc"
cba

bacd c bc

Output: "acdb"


monotonically inceasing stack


"""

def asd(st):
    a = set()
    l, r = 0 , 0

    res = st
    while r<st.__len__():
        if not st[r] in a:
            ...
        
        r+=1

b--c---a

asd("bcabc") 
abc---> bca
r = 0
b --> set(b)
r+=1
c--> set(b, c)
r+=1
a--> set(a, b,c)
r+=1
b<-- set()
