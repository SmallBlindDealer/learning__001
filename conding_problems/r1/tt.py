"""


1. In-Memory Key Value (KV) Store

Design and implement an in-memory key value datastore. 
This datastore should be able to support some basic operations such as Get, 
Set and Delete for string keys and any values.

You can assume that the input operations are always valid, 
but the key to operate on may be non-existent. We won’t worry 
about concurrent access to the database. You can handle errors 
however you think is best.

Let’s start with the data structure of this key value store. 
Implement methods for Get, Set and Delete.


Then Support Transactions and  multiple transactions
A transaction is created with the Begin command and creates a context 
for the other operations to happen. Until the active transaction is 
committed using the Commit command, those operations do not persist. 
And, the Rollback command throws away any changes made by those 
operations in the context of the active transaction.

Commit() and Rollback() will only happen when inside a transaction.

I would like to see test cases as well as implementation code.

Bonus: 
——> Add On after the above question. Nested Transaction? 



Set a = 1 -> db (a= 1)
Set b = 2 -> db (a= 1,b = 2)

Begin 
Set a = 5 ->  db (a= 1,b = 2)
Set b = 6 ->  db (a= 1,b = 2)
get a   -> 5
Commit  ->  db (a= 5,b = 6)
get     --> 5

Begin 
Set a = 8 ->  db (a= 5,b = 6)
Set b = 9 ->  db (a= 5,b = 6)
RollBak ->  db (a= 5,b = 6)


 Get
 Set
 Delete

Commit()
Rollback()

"""

class InMemoryKeyStorage:
    def __init__(self):
        self.data = {}
        self.txn_data = {} # uuid--{}
        self.is_txn = False
    
    def begin(self):
        self.is_txn = True
    
    def commit(self):
        for k, v in self.txn_data.items():
            self.data[k] = v
        self.is_txn = False

    def roll_back(self):
        self.txn_data = {}
        self.is_txn = False

    def get(self, k):
        if self.is_txn and k in self.txn_data: #here we have to look how to handle txn or without txn
            return self.txn_data[k]
        elif k in self.data:
            return self.data[k]
        else:
            raise Exception("given key doesn't exist")
    
    def set(self, k, v):
        if self.is_txn:
            self.txn_data[k] = v
        else:
            self.data[k] = v
        
    def delete(self, k):
        if self.is_txn and k in self.txn_data:
            del self.txn_data[k]
        elif k in self.data:
            del self.data[k]
        else:
            raise Exception("given key doesn't exist")



