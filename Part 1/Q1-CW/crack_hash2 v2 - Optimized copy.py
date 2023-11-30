import time , os
from hashlib import sha256
from itertools import permutations

cnt = 0

def counter(word, num_set, symbol_set):
    global cnt, start_time

    for num in num_set:
        for symbol in symbol_set:
            new_word = f"{word}{num}{symbol}"
            for perm in permutations(new_word):
                if perm[0] not in num_set and perm[0] not in symbol_set and perm[0] != word[0]:
                    continue
                
                cnt += 1    
                print(f'current count : {cnt}' , flush=True, end="\r")




with open("Q1-CW/dictionary") as f:
    dictionary = f.readlines()

num_set = set('0123456789')
symbol_set = set('&=!?.~*^#$')

for word in sorted(dictionary, key=len):
    word = word.strip()
    counter(word, num_set, symbol_set)

print("*" * 80)
print(f"Number of attempts: {cnt}")
