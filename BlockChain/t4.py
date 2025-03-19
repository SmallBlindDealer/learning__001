import json
from cryptography.fernet import Fernet

# For demonstration, we generate a key.
# In production, securely generate and store your key.
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

def encrypt_block_data(block_data, prev_encrypted):
    """
    Takes a dictionary for block_data and the previous block's encrypted string,
    packs them into a JSON payload, and returns the encrypted payload.
    """
    payload = {
        'block_data': block_data,
        'prev_encrypted': prev_encrypted.decode() if prev_encrypted else None
    }
    encoded_payload = json.dumps(payload).encode()
    encrypted_payload = cipher.encrypt(encoded_payload)
    return encrypted_payload

def decrypt_block_data(encrypted_payload):
    """
    Decrypts the encrypted payload and returns the corresponding JSON object.
    """
    decrypted_payload = cipher.decrypt(encrypted_payload)
    return json.loads(decrypted_payload)

def retrieve_blockchain_data(latest_encrypted_str, block_number):
    """
    Given the encrypted string of the latest block and a block number,
    this function iterates (or recurses) to retrieve all block data.
    
    Parameters:
      - latest_encrypted_str: The encrypted string (as bytes) for the current block.
      - block_number: An integer indicating the current block's number.
      
    Returns:
      A list of block data dictionaries (from latest to genesis).
    """
    blocks = []
    current_encrypted = latest_encrypted_str
    current_block_number = block_number
    
    while current_encrypted is not None and current_block_number >= 0:
        print(len(current_encrypted))
        try:
            block = decrypt_block_data(current_encrypted)
        except Exception as e:
            print(f"Error decrypting block {current_block_number}: {e}")
            break

        blocks.append(block['block_data'])
        
        # Get the previous block's encrypted string (if any)
        prev_enc_str = block.get('prev_encrypted')
        current_encrypted = prev_enc_str.encode() if prev_enc_str else None
        current_block_number -= 1
        
    return blocks

# Example usage: Create a simple chain of 3 blocks.
def create_sample_chain():
    # Genesis block (block 0)
    genesis_data = {"info": "Genesis Block"}
    genesis_encrypted = encrypt_block_data(genesis_data, None)
    
    # Block 1: Use genesis_encrypted as pointer.
    block1_data = {"info": "Block 1 Data", "value": 123}
    block1_encrypted = encrypt_block_data(block1_data, genesis_encrypted)
    
    # Block 2: Use block1_encrypted as pointer.
    block2_data = {"info": "Block 2 Data", "value": 456}
    block2_encrypted = encrypt_block_data(block2_data, block1_encrypted)
    
    
    # Block 3: Use block1_encrypted as pointer.
    block3_data = {"info": "Block 3 Data", "value": 4}
    block3_encrypted = encrypt_block_data(block3_data, block2_encrypted)
    
    # Return the latest block and its block number.
    return block3_encrypted, 2

# Create the chain and retrieve all block data.
latest_encrypted, block_num = create_sample_chain()
all_blocks = retrieve_blockchain_data(latest_encrypted, block_num)

print("Retrieved Blocks (from latest to genesis):")
for i, block in enumerate(all_blocks[::-1]):
    print(f"Block {i}: {block}")


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

