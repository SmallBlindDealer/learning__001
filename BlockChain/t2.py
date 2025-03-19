import hashlib
import json
import time
import base64
from cryptography.fernet import Fernet

# Generate a secret key for encryption/decryption (use a fixed key for real-world applications)
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

class Block:
    def __init__(self, index, previous_hash, encrypted_data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.encrypted_data = encrypted_data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.encrypted_data}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def to_dict(self):
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "encrypted_data": self.encrypted_data.decode(),  # Convert bytes to string
            "encrypted_data_len": len(self.encrypted_data.decode()),  # Convert bytes to string
            "timestamp": self.timestamp,
            "hash": self.hash
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "0", cipher.encrypt("Genesis Block".encode()))
    
    def add_block(self, data):
        last_block = self.chain[-1]
        encrypted_data = cipher.encrypt(data.encode())  # Encrypt data
        new_block = Block(len(self.chain), last_block.hash, encrypted_data)
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=4))
    
    def decode_chain(self):
        decrypted_data = []
        for block in self.chain[1:]:  # Skipping genesis block
            decrypted_data.append(cipher.decrypt(block.encrypted_data).decode())
        return "\n".join(decrypted_data)

# Example Usage
def store_and_retrieve_data():
    blockchain = Blockchain()
    
    for _ in range(100):
        # Adding some data
        blockchain.add_block("Hello, Blockchain!")
        blockchain.add_block("This is encrypted storage.")
        blockchain.add_block("Each block stores encrypted data.")

    print("\n🔗 Blockchain with Encrypted Data:")
    blockchain.print_chain()

    print("\n🔓 Decoded Data:")
    print(blockchain.decode_chain())

# Run Example
store_and_retrieve_data()
