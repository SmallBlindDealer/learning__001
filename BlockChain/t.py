import hashlib
import json
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self):
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "data": self.data,
            "timestamp": self.timestamp,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")
    
    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, data)
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=4))
    
    def decode_chain(self):
        return "\n".join(block.data for block in self.chain[1:])  # Skipping genesis block

# Example usage
def store_file_in_blockchain(file_path):
    blockchain = Blockchain()
    
    with open(file_path, 'r') as file:
        for line in file:
            blockchain.add_block(line.strip())
    
    blockchain.print_chain()
    
    print("\nDecoded File Data:")
    print(blockchain.decode_chain())

# Run Example
if __name__=="__main__":
    file_path = "./BlockChain/sample.txt"  # Create a sample.txt with some lines before running
    # import os
    # print(os.getcwd())
    store_file_in_blockchain(file_path)
