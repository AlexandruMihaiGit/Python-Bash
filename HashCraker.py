import hashlib

wordlist_location = input('Enter wordlist file location: ')
hash_input = input('Enter hash to be cracked: ')

if len(hash_input) != 32:
    print("Error: The hash does not appear to be a valid MD5 hash")
    exit(1)

try:
    with open(wordlist_location, 'r') as file:
        found = False
        for line in file:
            word = line.strip()
            hashed_pass = hashlib.md5(word.encode()).hexdigest()
            if hashed_pass == hash_input:
                print(f"Found password! {word}")
                found = True
                break
        if not found:
            print("Password not found in wordlist.")
except FileNotFoundError:
    print(f"Error: The file at {wordlist_location} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
