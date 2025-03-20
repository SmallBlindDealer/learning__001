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


Bonus: 
——> Add On after the above question. Nested Transaction? 



Begin 
Set a = 5 ->  db (a= 1,b = 2)
Set b = 6 ->  db (a= 1,b = 2)



Commit  ->

func--txn-->extend--another_txn--> 
"""
import uuid



class InMemoryKeyStorage:
    def __init__(self):
        self.data = {}
        self.txn_data = {} # uuid--{}
    
    
    def begin(self):
        unique_id = str(uuid.uuid4())
        while unique_id in self.txn_data:
            unique_id = str(uuid.uuid4())
        self.txn_data[unique_id] = {}
        return unique_id
    
    def commit(self, uuid=None):
        if uuid and uuid in self.txn_data:
            for k, v in self.txn_data[uuid].items():
                self.data[k] = v
        else:
            raise Exception("invalid request")


    def roll_back(self, uuid=None):
        if uuid in self.txn_data:
            del self.txn_data[uuid]
        else:
            raise Exception("invalid request")


    def get(self, k, uuid=None):
        if uuid:
            if uuid in self.txn_data: #here we have to look how to handle txn or without txn
                if k in self.txn_data[uuid]:
                    return self.txn_data[uuid][k]
            else:
                raise Exception("invalid request")
        elif k in self.data:
            return self.data[k]

        raise Exception("given key doesn't exist")
    
    def set(self, k, v, uuid=None):
        if uuid:
            if uuid in self.txn_data:
                self.txn_data[uuid][k] = v
        else:
            self.data[k] = v
        
    def delete(self, k, uuid=None):
        if uuid:
            if k in self.txn_data[uuid]:
                del self.txn_data[k]
        elif k in self.data:
            del self.data[k]

        raise Exception("given key doesn't exist")



in_memo_obj = InMemoryKeyStorage()
in_memo_obj.set("a", 1)
in_memo_obj.set("b", 2)
print(f"a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")

txn_1 = in_memo_obj.begin()
in_memo_obj.set("a", 5, txn_1)
in_memo_obj.set("b", 6, txn_1)
in_memo_obj.commit(txn_1)

print(f"a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")

txn_2 = in_memo_obj.begin()
in_memo_obj.set("a", 8, txn_2)
in_memo_obj.set("b", 9, txn_2)
in_memo_obj.roll_back(txn_2)

print(f"a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")




txn_1 = in_memo_obj.begin()
txn_2 = in_memo_obj.begin()

in_memo_obj.set("a", 6, txn_1)
in_memo_obj.set("b", 7, txn_1)

in_memo_obj.set("a", 8, txn_2)
in_memo_obj.set("b", 9, txn_2)

print(f"from txn_1 perspective --> a: {in_memo_obj.get('a', txn_1)} | b: {in_memo_obj.get('b', txn_1)}")
print(f"from txn_2 perspective --> a: {in_memo_obj.get('a', txn_2)} | b: {in_memo_obj.get('b', txn_2)}")

print(f"in db--> a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")

in_memo_obj.commit(txn_1)
print(f"in db--> a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")
in_memo_obj.commit(txn_2)
print(f"in db--> a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")

# in_memo_obj.commit(txn_1)

# print(f"a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")

# in_memo_obj.roll_back(txn_2)

# print(f"a: {in_memo_obj.get('a')} | b: {in_memo_obj.get('b')}")


"""


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