import csv

with open('info.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

a = []
for i in data:
    a.append(int(i[0]))

def get_sum(a, window):
    last, count = -1, -1
    for i in range(0, len(a)-window+1):
        s = sum(a[i:i+window])
        if s > last:
            count += 1
        last = s
    return count

print(get_sum(a, 1))
print(get_sum(a, 3))
