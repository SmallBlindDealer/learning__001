"""
There's a staircase with n steps, and you can climb up either 1 or 2 steps
 at a time.Given an integer n which represents the total number of steps,
   write a function that returns the number of unique ways you can climb the staircase.
     The order of the steps matters, so each different order of steps counts as a way.

    n=5

Input: n = 1
Output: 1
Input: n = 3
Output: 3
Input: n = 4
Output: 5

"""

def asd(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    return asd(n-1) + asd(n-2)


def total_path_list(n):
    if n==1:
        return [[1]]
    if n==2:
        return [[1,1], [2]]
    
    res_1 =  total_path_list(n-1)
    res_2 =  total_path_list(n-2)
    r = []
    for obj in res_1:
        r.append(obj+[1])

    for obj in res_2:
        r.append(obj+[2])

    return r


# print(asd(5), total_path_list(5))



"""
Given a two-dimensional integer matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, 
so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.
Note: Neighbors can only be directly horizontal or vertical, not diagonal.
Constraints
n, m ≤ 100 where n and m are the number of rows and columns in the matrix.

Example 1
Input
matrix = [
    [1, 1],
    [1, 0]
]
Output
1
Example 2
Input
matrix = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]
Output
4
Example 3
Input
matrix = [
    [0, 1],
    [1, 0]
]
Output
2

"""


matrix = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]

def find_total_island(matrix):

    total_island = 0
    row_l = matrix.__len__()
    col_l = matrix[0].__len__()

    visited_set = set()

    def dfs(row, col):
        if (row, col) in visited_set or row>=row_l or col>=col_l or row<0 or col<0 or matrix[row][col]!=1:
            return False
        
        visited_set.add((row, col))

        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col+1)
        dfs(row, col-1)
        
        return True
    
    
    for row in range(row_l):
        for col in range(col_l):
            if matrix[row][col]==1:
                if dfs(row, col):
                    total_island += 1
        

    return total_island


print(find_total_island([
    [1, 1],
    [1, 0]
])==1)
print(find_total_island([
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
])==4)
print(find_total_island([
    [0, 1],
    [1, 0]
])==2)

print(find_total_island([
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1]
]))