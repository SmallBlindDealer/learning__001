



# 0,1,1,2,3, 5


fib_collection = {}
fib_collection = {1:0, 2:1}

def fib2(n):
    if n in fib_collection:
        return fib_collection[n]
    
    if n<1:
        return 0
    if n==1:
        return 0
    if n==2:
        return 1
    
    fib_collection[n] = fib(n-1)+fib(n-2)
    return fib_collection[n]


def fib(n):
    # if n==0:
    c0 = 0
    c1 = 1
    
    while n-2>0:
        c0, c1 = c1, (c0+c1)
        n-=1
    
    return c1
    

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(10))
print(fib(11))
print(fib(12))
print(fib(100))




"""
TableA--id--1,2,3,4,5
TableB--id--1,2,3

SELECT a.id 
from TableA a 
left JOIN ON a.id<>b.id
TableB b;




SELECT a.id
from TableA a 
left JOIN ON
TableB b a.id=b.id
WHERE b.id==NULL;




"""

"""







"""