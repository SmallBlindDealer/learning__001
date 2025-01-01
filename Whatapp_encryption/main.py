from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Step 1: Key Generation
def generate_keys():
    key = RSA.generate(2048)  # Generate RSA keys
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Step 2: Simulating Key Exchange
def exchange_keys(sender_pub_key, recipient_pub_key):
    # Public keys are shared between sender and recipient
    return sender_pub_key, recipient_pub_key

# Step 3: Encrypt a message
def encrypt_message(message, recipient_pub_key):
    public_key = RSA.import_key(recipient_pub_key)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(encrypted_message).decode('utf-8')

# Step 4: Decrypt a message
def decrypt_message(encrypted_message, recipient_private_key):
    private_key = RSA.import_key(recipient_private_key)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode('utf-8')

# Demonstration
if __name__ == "__main__":
    # Generating keys for both sender and recipient
    sender_private_key, sender_public_key = generate_keys()
    recipient_private_key, recipient_public_key = generate_keys()

    # Exchange public keys
    _, recipient_pub_key = exchange_keys(sender_public_key, recipient_public_key)

    # Sender encrypts a message using the recipient's public key
    message = "Hello, this is a secure message!"
    encrypted_msg = encrypt_message(message, recipient_pub_key)
    print(f"Encrypted Message: {encrypted_msg}")

    # Recipient decrypts the message using their private key
    decrypted_msg = decrypt_message(encrypted_msg, recipient_private_key)
    print(f"Decrypted Message: {decrypted_msg}")
