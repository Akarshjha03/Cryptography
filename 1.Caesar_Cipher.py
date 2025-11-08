def caesar_encrypt_with_keylist(text, key_list):
    result = ""
    key_len = len(key_list)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = key_list[i % key_len]
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result


def caesar_decrypt_with_keylist(text, key_list):
    inverse_key_list = [-k for k in key_list]
    return caesar_encrypt_with_keylist(text, inverse_key_list)

# Formula = (P + K) mod 26.


# Example usage
plain_text = "Secure Message!"
key_list = [3, 1, 4, 2]  # Rotating key sequence

encrypted_text = caesar_encrypt_with_keylist(plain_text, key_list)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_decrypt_with_keylist(encrypted_text, key_list)
print("Decrypted:", decrypted_text)
