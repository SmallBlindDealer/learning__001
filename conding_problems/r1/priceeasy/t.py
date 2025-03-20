"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


"""

from collections import deque
import heapq

def kthLargestValue(nums, k):
    res = nums[:k]

    for obj in nums[k:]:
        curr = heapq.heappop(res)
        if curr<obj:
            heapq.heappush(res, obj)
        else:
            heapq.heappush(res, curr)
    
    return heapq.heappop(res)
        

print(kthLargestValue(nums = [3,2,1,5,6,4], k = 2)==5)
print(kthLargestValue(nums = [3,2,3,1,2,4,5,5,6], k = 4)==4)

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: 
# Output: 4

import pandas as pd

product_ = pd.read_csv("./product.csv")
sales_ = pd.read_csv("./product.csv")


def get_pdt_name_from_desc(string_: str):
    string_ = string_.split(" ")
    pdt_code = string_[-1]
    final = []
    for ch in pdt_code:
        if ch.isalnum():
            final.append(final)
    
    return "-".join([str(final[:2]), str(final[2:6]) + str(final[6:])])

sales_["product_id"] = sales_["description"].apply(lambda x: get_pdt_name_from_desc(x))

result = pd.merge(sales_, product_, on="product_id", how="left")

sales_summary = result.groupby('category')['amount'].sum().reset_index()

print(sales_summary)
