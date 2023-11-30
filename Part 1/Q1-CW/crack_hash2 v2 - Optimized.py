import time
import os
from hashlib import sha256
from itertools import permutations

# CLI Foreground Colors
class Fore:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[39m'
    BOLD = '\033[1m'
    YELLOW = '\033[93m'

# Hash and dictionary file paths
hash_file_path = "./hash_to_crack2/Hash2_Ahmed_Basem"
dictionary_file_path = "./dictionary"

num_set = set('0123456789')
symbol_set = set('&=!?.~*^#$')

# Counter Variable Intialization
cnt = 0

# Welcome Message
print(f"{Fore.BOLD}Welcome to Enhanced Hash Cracker - Ahmed Basem - 202000188{Fore.RESET}")
# Separator
print(80 * '-')


# Crack function
def crack(word, hash):
    global cnt, start_time

    for num in num_set:
        for symbol in symbol_set:
            new_word = f"{word}{num}{symbol}"
            for perm in permutations(new_word):
                # Check conditions for valid permutations
                if perm[0] not in num_set and perm[0] not in symbol_set and perm[0] != word[0]:
                    continue
                cnt += 1
                if hash in sha256("".join(perm).encode()).hexdigest():
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    # Print progress and result
                    print(f"Trying: {word}, Attempts: {Fore.YELLOW}{cnt}{Fore.RESET}, Elapsed Time: {Fore.YELLOW}{elapsed_time:.2f} seconds{Fore.RESET}")
                    print(80 * '-')
                    
                    # Print colored output
                    print(f"{Fore.GREEN}Password found!{Fore.RESET}")
                    print(f"Number of attempts: {Fore.YELLOW}{cnt}{Fore.RESET}")
                    print(f"The hash corresponds to: {Fore.RED}{''.join(perm)}{Fore.RESET}")
                    print(f"Password: {Fore.RED}{word}{Fore.RESET} --> {Fore.RED}{''.join(perm)}{Fore.RESET}")
                    print(f"Time taken to search: {Fore.YELLOW}{elapsed_time:.2f} seconds{Fore.RESET}")
                    
                    # Print final separator and exit the program
                    print(80 * '-')
                    exit()



# Read dictionary and hash
with open(dictionary_file_path) as f:
    dictionary = f.readlines()
with open(hash_file_path) as hash_file:
    hash_value = hash_file.readline().strip()


# Start time and print the target hash
start_time = time.time()
print(f"Hash to crack: {Fore.RED}{hash_value}{Fore.RESET}")

# Iterate through the dictionary and attempt to crack the hash
for word in sorted(dictionary, key=len):
    word = word.strip()
    # Print progress
    print(f"Trying: {word}, Attempts: {Fore.YELLOW}{cnt}{Fore.RESET}, Elapsed Time: {Fore.YELLOW}{(time.time() - start_time):.2f} seconds{Fore.RESET}", flush=True, end="\r")
    # Attempt to crack the hash
    crack(word, hash_value)

# Final separator
print(80 * '-')
