

"""

fib

1-->0
2-->1
3-->1

"""

cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    
    
    if n==1:
        cache[1] = 0
        print(cache[n])
        return cache[n]
    
    elif n==2:
        cache[n] = 1 + fib(1)
        print(cache[n])
        return cache[n]
    
    cache[n] = fib(n-1) +fib(n-2)
    print(cache[n])
    return     cache[n]
    

fib(10)


"""
paytam wallet
crud--acc
money
txn history
check wallet


UserInfo:
    CRUD account
    id
    name
    number

WalletInfo:
    id
    user_id
    current_amount

100k users may come as concurent..any time
monthly--1000k
---highly cosistent system
---raplica of server will erver availability...and replica of db..
--
Transaction:
    id

    
InputTransaction:
    ...


    
---backend arch
--high problems
--

"""