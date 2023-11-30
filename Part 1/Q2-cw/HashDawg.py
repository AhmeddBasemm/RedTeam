import os
import argparse
from hashlib import sha1
from time import time

# CLI Foreground Colors
class Fore:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[39m'
    BOLD = '\033[1m'
    YELLOW = '\033[93m'

# Hash Cracker Class
class HashCracker:
    def __init__(self, wordlist, hashlist, output_file, dictionary_file):
        """
        Initialize HashCracker with file paths and data structures.
        """
        # Initialize instance variables
        self.wordlist = wordlist
        self.hashlist = hashlist
        self.output_file = output_file
        self.dictionary_file = dictionary_file
        self.passwords = []
        self.hashes = []
        self.hashdict = {}
        self.counter = 0

        # Display program header
        print(f"{Fore.BOLD}HashDawg by Ahmed Basem - 202000188{Fore.RESET}")

    def load_wordlist(self):
        """
        Load passwords from the wordlist file.
        """
        try:
            # Open and read the wordlist file
            with open(self.wordlist, "r", encoding="UTF-8", errors="ignore") as f:
                # Store passwords in a list
                self.passwords = [line.strip() for line in f]
        except FileNotFoundError:
            # Display an error message if the wordlist file is not found
            print(f"{Fore.RED}Error: Wordlist file '{self.wordlist}' not found.{Fore.RESET}")
            exit(1)

    def load_hashlist(self):
        """
        Load hashes from the hashlist file.
        """
        try:
            # Open and read the hashlist file
            with open(self.hashlist, "r", encoding="UTF-8") as f:
                # Store hashes in a list
                self.hashes = [line.strip() for line in f]
        except FileNotFoundError:
            # Display an error message if the hashlist file is not found
            print(f"{Fore.RED}Error: Hashlist file '{self.hashlist}' not found.{Fore.RESET}")
            exit(1)

    def load_hash_dictionary(self):
        """
        Load or create a hash dictionary for efficient lookup.
        """
        # Display separator line
        print(f"{Fore.YELLOW}-" * 40)
        start_time = time()

        try:
            if os.path.exists(self.dictionary_file):
                # If dictionary file exists, load it
                print(f"{Fore.GREEN}Hash dictionary found!{Fore.RESET}")
                print("Loading hash dictionary...")

                with open(self.dictionary_file, "r", encoding="UTF-8", errors="ignore") as f:
                    # Populate hash dictionary from file
                    for line in f:
                        passwd, hash_value = line.rsplit(":", 1)
                        self.hashdict[hash_value.strip()] = passwd.strip()
            else:
                # If dictionary file doesn't exist, create it
                print(f"{Fore.RED}Hash dictionary not found!{Fore.RESET}")
                print("Creating hash dictionary...")

                with open(self.dictionary_file, "w", encoding="UTF-8", errors="ignore") as f:
                    # Populate hash dictionary and write to file
                    for passwd in self.passwords:
                        passwd = passwd.strip()
                        hashed = sha1(passwd.encode()).hexdigest()
                        f.write(f"{passwd}:{hashed}\n")
                        self.hashdict[hashed] = passwd
        except FileNotFoundError:
            # Display an error message if the dictionary file is not found
            print(f"{Fore.RED}Error: Hash dictionary file '{self.dictionary_file}' not found.{Fore.RESET}")
            exit(1)

        # Display dictionary loading information
        print(f"Hash dictionary loaded with {Fore.GREEN}{len(self.hashdict)}{Fore.RESET} entries")
        end_time = time()
        print(f"time taken: {Fore.GREEN}{(end_time - start_time):.2f}{Fore.RESET} seconds")
        print(f"{Fore.YELLOW}{'-'*40}{Fore.RESET}")

    def extract_passwords(self):
        """
        Extract passwords from hashes and save to an output file.
        """
        with open(self.output_file, "w", encoding="UTF-8", errors="ignore") as s:
            print("Extracting passwords...")
            start_time = time()

            for hash_value in self.hashes:
                hash_value = hash_value.strip()
                if hash_value in self.hashdict:
                    # If hash is found in the dictionary, extract and save the password
                    passwd = self.hashdict[hash_value]
                    s.write(f"{passwd}:{hash_value}\n")
                    self.counter += 1

            end_time = time()
            # Display extraction results and time taken
            print(f"Extracted {Fore.GREEN}{self.counter}{Fore.RESET} passwords from {len(self.hashes)}")
            print(f"Done! - time taken: {Fore.GREEN}{(end_time - start_time):.2f}{Fore.RESET} seconds")
            print(f"{Fore.YELLOW}{'-'*40}{Fore.RESET}")
            print(f"Extracted passwords saved to  ----> {self.output_file}")
            print(f"{Fore.YELLOW}{'-'*40}{Fore.RESET}")

# Main function
def main():
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Hash Cracker")
    parser.add_argument("wordlist", nargs="?", default="rockyou.txt", help="Path to the wordlist file")
    parser.add_argument("hashlist", nargs="?", default="LinkedIn_HalfMillionHashes.txt", help="Path to the hashlist file")
    parser.add_argument("--output", default="Extracted.txt", help="Output file name")
    parser.add_argument("--dictionary", default="hashdict.txt", help="Hash dictionary file name")

    # Parse command-line arguments
    args = parser.parse_args()

    # Create HashCracker instance
    cracker = HashCracker(args.wordlist, args.hashlist, args.output, args.dictionary)

    # Load wordlist, hashlist, and hash dictionary
    cracker.load_wordlist()
    cracker.load_hash_dictionary()

    #load Target hashlist
    cracker.load_hashlist()

    # Extract passwords and display results
    cracker.extract_passwords()

if __name__ == "__main__":
    main()
