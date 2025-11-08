import os

def generate_key(length):
    """Generate a truly random key of given length (cryptographically secure)."""
    return os.urandom(length)

def encrypt(plaintext, key):
    """Encrypt plaintext using XOR with OTP key."""
    p_bytes = plaintext.encode('utf-8')
    return bytes([p ^ k for p, k in zip(p_bytes, key)])

def decrypt(ciphertext, key):
    """Decrypt ciphertext using XOR with OTP key."""
    p_bytes = bytes([c ^ k for c, k in zip(ciphertext, key)])
    return p_bytes.decode('utf-8')

if __name__ == "__main__":
    text = "HELLO WORLD"
    
    # Key must be same length as plaintext
    key = generate_key(len(text))
    
    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext : ", text)
    print("Key (hex) : ", key.hex())
    print("Encrypted : ", encrypted.hex())
    print("Decrypted : ", decrypted)
