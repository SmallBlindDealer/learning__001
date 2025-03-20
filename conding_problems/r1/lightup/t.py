"""

Create a datastructure
list, set---Insert (int v) -> if the value exists return false
set----Delete(int v) -> if the value exists delete and return true else return false and 
----getRandom() -> if there are 100 elements 
getRandom if its called 100 times, each element should be returned with
Equal probability 

O(1) ->
"""

import random

class RandomizedSet:

	def __init__(self):
		self.value_idx_map = dict()
		self.values = []
		
		
        """
		1--0,2--1,3--2
		
		remove 2
        [1,2,3]-->[1,3,2]
		
		random.choice()
		2-->-1
		
		
		"""
		# self.

	def insert(self, val: int) -> bool:
		if val in self.value_idx_map:
			return False
		else:
			self.values.append(val)
			self.value_idx_map[val] = self.value_idx_map.__len__()-1
			return True


	def remove(self, val: int) -> bool:
		if val 
		
		# if val in self.self.:
		# 	self.values.remove(val)
		# 	return True
		# else:
		# 	return False   	 

	def getRandom(self) -> int:
		if self.values:
		    return random.choice(list(self.values))
	
		

obj = RandomizedSet()
[obj.insert(i) for i in range(20)]

print(obj.getRandom())