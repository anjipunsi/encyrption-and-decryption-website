# transposition_cipher.py
class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        encrypted_message = ''
        for i in range(self.key):
            encrypted_message += message[i::self.key]
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = [''] * len(encrypted_message)
        rows = len(encrypted_message) // self.key
        cols = self.key
        full_rows = len(encrypted_message) % self.key

        for i in range(full_rows):
            decrypted_message[i * (rows + 1)] = encrypted_message[i]

        offset = full_rows * (rows + 1)
        for i in range(cols - full_rows):
            decrypted_message[offset + i * rows: offset + (i + 1) * rows] = encrypted_message[full_rows + i::cols]

        return ''.join(decrypted_message)
