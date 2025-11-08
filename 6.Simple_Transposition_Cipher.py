import math

def get_key_order(key):
    key = str(key).upper()
    return sorted(range(len(key)), key=lambda x: key[x])

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    col = len(key)
    row = math.ceil(len(plaintext) / col)

    # Pad with X if needed
    plaintext += "X" * (row * col - len(plaintext))

    # Create matrix row-wise
    matrix = [list(plaintext[i:i+col]) for i in range(0, len(plaintext), col)]

    ciphertext = ""
    for col_index in get_key_order(key):
        for r in range(row):
            ciphertext += matrix[r][col_index]

    return ciphertext

def decrypt(ciphertext, key):
    col = len(key)
    row = math.ceil(len(ciphertext) / col)

    matrix = [[""] * col for _ in range(row)]

    index = 0
    for col_index in get_key_order(key):
        for r in range(row):
            matrix[r][col_index] = ciphertext[index]
            index += 1

    # Read row-wise
    plaintext = ""
    for r in range(row):
        for c in range(col):
            plaintext += matrix[r][c]

    return plaintext

# Example usage
if __name__ == "__main__":
    text = "HELLO WORLD"
    key = "3142"      # Numeric key as string
    # key = "SECRET"  # Or keyword key (will work too)

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext : ", text)
    print("Key       : ", key)
    print("Encrypted : ", encrypted)
    print("Decrypted : ", decrypted)
