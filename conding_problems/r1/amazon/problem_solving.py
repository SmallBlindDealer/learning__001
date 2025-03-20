// Q. find K-largest elements in the array
// eg. ar - [1,9,2,8,3,7], k = 3


-->merge sort-->NlogN
-->bububle sort-->N2


// eg. ar - [1,9,2,8,3,7], k = 9

def get_L_largest_elements(ar, k):
    
    if k>len(ar) or k<=0:
        return -1

    ar.sort() ---->nlong
    return ar[k-1]--->1
    
    --->NlogN


import heapq

def get_L_largest_elements_by_using_hq(ar, k):
    if k>len(ar) or k<=0:
        return -1
    
    stack = [-obj for obj in ar[:k]]

    for obj in ar[k:]:    --------------------> N
        cur = heapq.heappop(stack) ----------->logN
        if curr*-1>obj:
            heapq.heappush(stack, -1*obj)-----> 1
        else:
            heapq.heappush(stack, cur)--------> 1
            
    return -1*heapq.heappop(stack)
    
    N>logN

    
    
// Q. Implement pow()


def pow(root_val, degree):
    d = {}
    d[1] = root_val
    d[2] = d_1*d_1
    
    res=1
    c = 0
    while c<degree:
        
        
    
    return d[degree]
        ...
    ...

def pow(root_val, degree):
    new_degree = degree//2
    
    pow_1 = root_val
    pow_2 = pow_1 * pow_1
    



pow(3, 4)



















    
    
    
    
    
    
    
    
    


