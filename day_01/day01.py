import csv

with open('info.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

a = []
for i in data:
    a.append(int(i[0]))

def get_sum(a, window):
    prev, count = -1, 0
    for i in range(1, len(a)-window+1):
        s = sum(a[i:i+window])
        if s > prev:
            count += 1
        prev = s
    return count

print(get_sum(a, 1)) # solves first part
print(get_sum(a, 3)) # solves second part

# use cURL + inspect element to obtain data
