import hashlib
import json
import time
import zlib
from cryptography.fernet import Fernet

# Generate a secret key (store securely in production)
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

def compress_data(text: str) -> bytes:
    """Compress a string using zlib."""
    return zlib.compress(text.encode('utf-8'))

def decompress_data(data: bytes) -> str:
    """Decompress zlib-compressed bytes into a string."""
    return zlib.decompress(data).decode('utf-8')

class Block:
    def __init__(self, index, prev_encrypted_data, data, timestamp=None):
        self.index = index
        self.prev_encrypted_data = prev_encrypted_data  # Previous block's encrypted data pointer
        # Compress the plaintext data first
        compressed_plaintext = compress_data(data)
        # Encrypt the compressed plaintext
        encrypted = cipher.encrypt(compressed_plaintext)
        # Additionally, compress the encrypted data (even if savings may be minimal)
        compressed_encrypted = zlib.compress(encrypted)
        self.encrypted_data = compressed_encrypted
        self.timestamp = timestamp or time.time()
    
    def to_dict(self):
        return {
            "index": self.index,
            "prev_encrypted_data": self.prev_encrypted_data.decode() if self.prev_encrypted_data else None,
            "encrypted_data": self.encrypted_data.hex(),  # Represent as hex for readability
            "timestamp": self.timestamp
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, None, "Genesis Block")
    
    def add_block(self, data):
        last_block = self.chain[-1]
        # Use the last block's encrypted data as the pointer for the new block
        new_block = Block(len(self.chain), last_block.encrypted_data, data)
        self.chain.append(new_block)
    
    def print_chain(self):
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=4))
    
    def decode_chain(self):
        """Decode the blockchain: first decompress outer layer from encrypted data,
           then decrypt, and finally decompress the plaintext."""
        decrypted_data = []
        for block in self.chain:
            # Remove outer compression: decompress the encrypted data
            decrypted_encrypted = zlib.decompress(block.encrypted_data)
            # Decrypt the inner (already compressed) plaintext
            compressed_plaintext = cipher.decrypt(decrypted_encrypted)
            # Decompress the plaintext to recover original data
            original = decompress_data(compressed_plaintext)
            decrypted_data.append(original)
        return "\n".join(decrypted_data)

# Example usage: store each line from a file as a block in the blockchain.
def store_file_in_blockchain(file_path):
    blockchain = Blockchain()
    with open(file_path, 'r') as file:
        for line in file:
            blockchain.add_block(line.strip())
    print("\n--- Blockchain ---")
    blockchain.print_chain()
    print("\n--- Decoded File Data ---")
    # print(blockchain.decode_chain())

# To run the example, uncomment the lines below and provide a valid file path:
file_path = "./BlockChain/sample.txt"  # Create a sample.txt with some lines before running
store_file_in_blockchain(file_path)
