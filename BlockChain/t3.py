import hashlib
import json
import time
from cryptography.fernet import Fernet

# Generate a secret key (this should be stored securely in real applications)
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

class Block:
    def __init__(self, index, prev_encrypted_data, data, timestamp=None):
        self.index = index
        self.prev_encrypted_data = prev_encrypted_data  # Store previous block's encrypted data
        self.encrypted_data = cipher.encrypt(data.encode())  # Encrypt current block's data
        self.timestamp = timestamp or time.time()
    
    def to_dict(self):
        return {
            "index": self.index,
            "prev_encrypted_data": self.prev_encrypted_data.decode() if self.prev_encrypted_data else "None",
            "encrypted_data": self.encrypted_data.decode(),
            "encrypted_data_len": len(self.encrypted_data.decode()),
            "timestamp": self.timestamp
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, None, "Genesis Block")  # First block has no previous encrypted data
    
    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.encrypted_data, data)  # Use prev block's encrypted data
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=4))
    
    def decode_chain(self):
        decrypted_data = []
        for block in self.chain:
            decrypted_data.append(cipher.decrypt(block.encrypted_data).decode())
        return "\n".join(decrypted_data)

# Example Usage
def store_and_retrieve_data():
    blockchain = Blockchain()
    
    # Adding some data
    blockchain.add_block("Hello, Blockchain!")
    blockchain.add_block("This is an encrypted blockchain.")
    blockchain.add_block("Each block stores encrypted data as hash.")

    print("\n🔗 Blockchain with Encrypted Data:")
    blockchain.print_chain()

    print("\n🔓 Decoded Data:")
    print(blockchain.decode_chain())

# Run Example
# store_and_retrieve_data()


# Example usage
def store_file_in_blockchain(file_path):
    blockchain = Blockchain()
    
    with open(file_path, 'r') as file:
        for line in file:
            blockchain.add_block(line.strip())
    
    blockchain.print_chain()
    
    # print("\nDecoded File Data:")
    # print(blockchain.decode_chain())

# Run Example
if __name__=="__main__":
    file_path = "./BlockChain/sample.txt"  # Create a sample.txt with some lines before running
    store_file_in_blockchain(file_path)
    # store_and_retrieve_data()
