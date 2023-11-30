import math

wordlist_size = 20000
average_word_length = 6.77

# Assuming each character in the wordlist can have a number (10 options) and a symbol (9 options) appended
choices_per_position = 10 + 9

# Calculate the total number of unique passwords
total_passwords = int(math.pow(choices_per_position, average_word_length) * wordlist_size)

# Format the output
print(f"Total number of unique passwords: {total_passwords:,}")
