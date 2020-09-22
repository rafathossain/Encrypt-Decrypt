import string

# Alphabet List
alphabet = list(string.ascii_uppercase)

# Encrypted List
encrypted = ['Z', 'A', 'Y', 'B', 'X', 'Z', 'A', 'Y', 'B', 'X', 'Z', 'A', 'Y', 'B', 'X', 'Z', 'A', 'Y', 'B', 'X', 'Z', 'A', 'Y', 'B', 'X', 'R']


# Python code to convert string to list character-wise
def Convert(data):
    list1 = []
    list1[:0] = data
    return list1


# Data encryption
def encryptData(data):
    encrypted_value = ""
    for alpha in Convert(data.upper()):
        encrypted_value += encrypted[alphabet.index(alpha)]
    return encrypted_value


# Data decryption
def decryptData(data):
    decrypted_value = ""
    for alpha in Convert(data.upper()):
        decrypted_value += alphabet[encrypted.index(alpha)]
    return decrypted_value


# Run the script
if __name__ == '__main__':
    option = input("Select Option:\n1. Encrypt\n2. Decrypt\n>>>")
    try:
        if int(option) == 1:
            print(encryptData(input("Enter data to encrypt: ")))
        elif int(option) == 2:
            print(decryptData(input("Enter data to decrypt: ")))
        else:
            print("Invalid input detected!")
    except Exception:
        print("Invalid data to encrypt/decrypt!")
