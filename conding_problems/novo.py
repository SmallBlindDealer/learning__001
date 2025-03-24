"""
2D sorted array..search eleement in aerray or not ..time ocomplel



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
Sample Output: true
Complexity - O(m+n) or O(m) or O(n)

m*log(n) > m+n >  logn+log(n/2)+log(n/4)......m



bundy search algo
"""

def returnMatch(arr, target):

    curr_col_idx = arr[0].__len__()-1

    for row in range(len(arr)): # -->m
        if arr[row][curr_col_idx]>target:
            # while True: #logn
            #     ...
            if returnMatch([obj[:curr_col_idx] for obj in arr], target):
                return True
        elif arr[row][curr_col_idx]==target:
            return True
        else:
            ...
    
    return False

    # while curr_row_idx<len(arr) and curr_col_idx>=0:

    #     while arr[curr_row_idx][curr_col_idx]>target:
    #         ...
    #     ...
    



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print(returnMatch(matrix, target))


"""
{"hot", "dot", "dog", "lot", "log", "cog"}
beginWord = "hit"----hot
                -----dot
                -----lot

                    
endWord = "cog"

{
    "*ot": [hot, dot, lot],
    "h*t": [hot],
    "ho*": [hot]

}

The shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog".

o/p: 5

heat-->head


beginWord = "cot"
endWord = "log"
o/p: 3
cot -> lot -> log

"""
from collections import defaultdict, deque

def shortest_transformation_sequence(seq, beginWord, endWord):
    if endWord not in seq:
        return -1
    
    adj_dict = defaultdict(list)
    for obj in seq:
        curr_str = [ch for ch in obj]
        for idx in range(len(curr_str)):
            adj_dict["".join(curr_str[:idx]) + "*" + "".join(curr_str[idx+1:])].append(obj)
    
    q = deque()
    q.append(beginWord)

    c = 0
    visited = set()

    while q:
        curr = q.popleft()

        if curr not in visited:
            visited.add(curr)

        for idx in range(len(curr)):
            curr_str = "".join(curr[:idx]) + "*" + "".join(curr[idx+1:])
            for word in adj_dict[curr_str]:
                if word == endWord:
                    return c
                if word not in visited:
                    q.append(word)
        
        c+=1


    return -1
    


seq = {"hot", "dot", "dog", "lot", "log", "cog"}
beginWord = "cot"
endWord = "log"
print(shortest_transformation_sequence(seq, beginWord, endWord))