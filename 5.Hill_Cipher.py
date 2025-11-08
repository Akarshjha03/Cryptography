import numpy as np

# Convert text to numbers (A = 0 ... Z = 25)
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

# Convert numbers to text
def numbers_to_text(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

# Matrix modular inverse for Hill Cipher
def matrix_mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))        # determinant
    det_inv = pow(det % modulus, -1, modulus)      # modular inverse of determinant
    adj = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus  # adjugate
    return (det_inv * adj) % modulus

# Encryption
def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.upper().replace(" ", "")
    
    # Pad with X if length not divisible by matrix size
    while len(plaintext) % n != 0:
        plaintext += 'X'
    
    nums = text_to_numbers(plaintext)
    cipher = []
    
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        encrypted_block = key_matrix.dot(block) % 26
        cipher.extend(encrypted_block)
    
    return numbers_to_text(cipher)

# Decryption
def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    nums = text_to_numbers(ciphertext)
    
    inv_key = matrix_mod_inverse(key_matrix, 26)
    plain = []
    
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        decrypted_block = inv_key.dot(block) % 26
        plain.extend(decrypted_block)
    
    return numbers_to_text(plain)

# Driver Program
if __name__ == "__main__":
    key_matrix = np.array([[3, 3],
                           [2, 5]])  # Must be invertible mod 26

    text = "HELLO"
    encrypted = encrypt(text, key_matrix)
    decrypted = decrypt(encrypted, key_matrix)

    print("Plaintext : ", text)
    print("Key Matrix:\n", key_matrix)
    print("Encrypted : ", encrypted)
    print("Decrypted : ", decrypted)
