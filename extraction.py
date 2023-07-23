
import csv
f = open('card.csv', 'r')
data = {}
keys = []
text = csv.reader(f)
header = next(text)


for i in text:
    for row in text:
        data[row[2]] = row[10].split(',')
        keys.append(row[2])
#print(keys)
keys = list(filter(lambda x: x != '', keys))


def keys_data(key):
    result = [float(num) for num in key if float(num) >= 50000]
    return result

extract = keys_data(keys)
print(extract)













