import csv

def extract_data():
    with open('card.csv', 'r') as f:
        data = {}
        keys = []
        text = csv.reader(f)
        header = next(text)

        for row in text:
            if row[2] != '':  # Check if the value in the third column is not empty
                data[row[2]] = row[1].split(',')
                keys.append(float(row[2]))
        
        #keys = list(filter(lambda x: x != '', keys))
        return keys

def keys_data(key):
    result = [float(num) for num in key if float(num) >= 500000]
    return result

if __name__ == '__main__':
    extract = extract_data()
    result = keys_data(extract)
    print(result)
