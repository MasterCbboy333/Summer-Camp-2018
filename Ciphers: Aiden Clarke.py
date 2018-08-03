ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def main():
    original = input("Enter the word to encrypt/decrypt: ").lower()
    key = int(input("Enter secret key: "))
   
    while True:
        choice = input("Would you like to encrypt or decrypt? ").lower()
        if choice.startswith("e"): 
            ciphertext = encrypt(original, key)
            print(ciphertext)
            break
        elif choice.startswith("d"):
            plaintext = decrypt(original, key)
            print(plaintext)
            break
        else:
            print("Unrecognized input")
   
def encrypt(original, key):
    secret_code = ""    # Empty variable for us to put our secret code in
    
    for letter in original:
        if letter.isalpha():   # Check to make sure the letter is actually a letter
            idx = (ALPHABET.index(letter) + key) % 26
            secret_code += ALPHABET[idx]
        else:
            secret_code += letter
            
    return secret_code

def decrypt(original, key):
    secret_code = ""    # Empty variable for us to put our secret code in
    
    for letter in original:
        if letter.isalpha():   # Check to make sure the letter is actually a letter
            idx = (ALPHABET.index(letter) - key) % 26
            secret_code += ALPHABET[idx]
        else:
            secret_code += letter
            
    return secret_code


main()  