import generate_key
import encryption
import decryption

if __name__ == '__main__':
    public_key, private_key = generate_key.generate_key_pair()

    message = "Pi:3141592653589793238565"

    encrypted_message = encryption.encrypt(message, public_key)
    print("Encrypted: ", encrypted_message)
    decrypted_message = decryption.decrypt(encrypted_message, private_key)
    print("Decrypted: ", decrypted_message)

