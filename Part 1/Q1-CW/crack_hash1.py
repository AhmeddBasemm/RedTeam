# Import necessary modules
from hashlib import sha256
import time

# CLI Foreground Colors
class Fore:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[39m'
    BOLD = '\033[1m'
    Yellow = '\033[93m'

# Print a separator line
print(80*'-')

# Welcome Message
print(f"{Fore.BOLD}Welcome to Hash Cracker - Ahmed Basem - 202000188{Fore.RESET}")

# File Paths
hash_file_path = "./hash_to_crack1/Hash1_Ahmed_Basem"
dictionary_file_path = "./dictionary"

# Read & Print Hash
with open(hash_file_path, "r") as f:
    target_hash = f.readlines()[0].strip()
    print(f"Target Hash: {Fore.RED}{target_hash}{Fore.RESET}")

# Start the timer
start_time = time.time()

# Enumerate & Hash Dictionary while Comparing with Target Hash
with open(dictionary_file_path, "r") as d:
    for (cnt, line) in enumerate(d):
        # Hash the word in the dictionary
        hashed_word = sha256(bytes(line.strip(), 'utf-8')).hexdigest()
        
        # Compare the hashed word with the target hash
        if target_hash == hashed_word:
            # Print Password if Found
            print(f"{Fore.BOLD}Password Found: {Fore.GREEN}{line.strip()}{Fore.RESET} at line {Fore.GREEN}{cnt}{Fore.RESET}")
            
            # Stop the timer
            end_time = time.time()

            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            break  # Exit the loop if the password is found

# Check if a password was found
if 'elapsed_time' in locals():
    print(f"{Fore.BOLD}Time taken to search: {Fore.Yellow} {elapsed_time:.2f} seconds{Fore.RESET}")
else:
    print(f"{Fore.BOLD}Password Not Found!{Fore.RESET}")

# Print a separator line
print(80*'-')
