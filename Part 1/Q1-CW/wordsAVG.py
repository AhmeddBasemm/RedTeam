#open dictionary file
f = open("Q1-CW/dictionary", "r")
if f.mode!='r': print("Something has gone wrong")

#loop through each line and add the length of the line to the sum
sum = 0
for (cnt, line) in enumerate(f):
    sum += len(str(line).strip())

#divide the sum by the number of lines to get the average
print(sum/cnt)