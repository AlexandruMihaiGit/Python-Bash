import requests
import sys
import os

def enumerate_directories(base_url, wordlist_file, extension="html"):
    if not os.path.isfile(wordlist_file):
        print(f"Error: {wordlist_file} not found.")
        sys.exit(1)

    with open(wordlist_file, "r") as f:
        directories = f.read().splitlines()

    for dir in directories:
        dir_enum = f"http://{base_url}/{dir}.{extension}"
        try:
            r = requests.get(dir_enum)
            if r.status_code == 200:
                print(f"Valid directory: {dir_enum}")
            elif r.status_code == 403:
                print(f"Forbidden directory: {dir_enum} (403)")
        except requests.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Use python3 DirectoryEnum.py <base_url> <wordlist_file> [extension]")
        sys.exit(1)

    base_url = sys.argv[1]
    wordlist_file = sys.argv[2]
    if len(sys.argv) > 3:
        extension = sys.argv[3]
    else:
        extension = "html"

    enumerate_directories(base_url, wordlist_file, extension)