
"""

"You are given a sequence of integers and a fixed window size K. 

For each position of the window as it slides over the sequence 
(from the start to the end), determine the highest integer visible 
within the window at that position."	

INPUT:
K = 3
numbers = [10, 3, -1, -3, 5, 3, 6, 7]

OUTPUT:
result = [3, 3, 5, 5, 6, 7]



numbers = [10, 3, -1, -3, 5, 3, 6, 7]

i=0
j=2

i=1
j=3


[10, 3, -1]
max_val = 10
max_val_idx = 0
res = []
for i in range(3, len(numbers)-2):
    if max_val_idx<i:
        ...
        max_val_idx = 1
        max_val = 3
        res.append()
    else:
        ...
"""

def return_max(arr: list, n):
    res = []
    first_max, secMax = sorted(arr[:n], reverse=True)[:2]
    first_max_idx = arr.index(first_max)
    sec_max_idx = arr.index(secMax)

    for i in range(0, len(arr)-n+1):
        if first_max_idx<i or sec_max_idx<i:
            if i<len(arr):
                first_max, secMax = sorted(arr[i:i+n], reverse=True)[:2]
                first_max_idx = arr.index(first_max)
                sec_max_idx = arr.index(secMax)


        res.append(arr[first_max_idx])

        if arr[i]>arr[first_max_idx]:
            first_max_idx, sec_max_idx = i, first_max_idx
        elif arr[i]>arr[sec_max_idx]:
            sec_max_idx = i
            ...
    

    return res

            

    


"""
K = 3
numbers = [10, 3, -1, -3, 5, 3, 6, 7]

OUTPUT:
result = [3, 3, 5, 5, 6, 7]



"""
print(return_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# 10, 3, 5, 


"""

"Given a array of string 

[geeksforgeeks, geetha, gesture, golang, geeky, generator] 

and a prefix word exmaple: ""gee"", output the number of string has this prefix.

IN - ""gee""
OP - 3

IN - ""ge""
OP - ""5""


"""

class Node:
    def __init__(self, ch):
        self.curr_char = ch
        self.isChild = False
        self.childs: dict[str:Node] = {}
        self.numbers_of_child_words = 0
    

class Trie:
    def __init__(self):
        self.words: dict[str:Node] = {}
    
    def add_word(self, word):
        curr_node = self.words[word[0]] if word[0] in self.words else Node(word[0])

        for i in range(1, len(word)):
            ...
    
