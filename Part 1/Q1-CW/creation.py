import sys
import random
import hashlib
import os
import binascii
import math
from math import floor

f = open("./dictionary", "r")
if f.mode!='r': print("Something has gone wrong")

list =[]

for (cnt, line) in enumerate(f):
    list.append(str(line).strip())

#Selection and hashing for question 12
pick = random.randint(0, len(list))

idf = open("./id.txt", "r")
if idf.mode!='r': print("Something has gone wrong")

id =[]
result =[]
result2 =[]
for (cnt, line) in enumerate(idf):
    id.append(str(line).strip())


for x in id:

	pick = random.randint(0, len(list))
	passwd2 = list[pick]

	numberset = ['0','1','2','3','4','5','6','7','8','9']
	symbolset=['&', '=', '!', '?', '.', '~', '*', '^', '#', '$']
	number = numberset[random.randint(0,len(numberset)-1)]
	location = random.randint(0,len(passwd2))
     
	passwd2 = passwd2[0:location]+number+passwd2[location:]
	symbol = symbolset[random.randint(0,len(symbolset)-1)]
	location = random.randint(0,len(passwd2))
	
	passwd2 = passwd2[0:location]+symbol+passwd2[location:]
	result2.append({x:passwd2})
	m = hashlib.sha256()
	m.update(bytes(passwd2, 'utf-8'))
	hash = m.hexdigest()
	f2 = open("hash2_"+str(x), "w")
	if f2.mode!='w': print("Something has gone wrong")
	f2.write(hash)
	f2.close()

print("password1")
print(result)
print("password2")
print(result2)
