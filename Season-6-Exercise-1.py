import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    inputData = []
    with open(input_file_name) as inputFile:        
        reader = csv.reader(inputFile)
        for row in reader:
            tmp = []
            tmp.append(row[0])
            tmp.append(row[1])
            inputData.append(tmp)

    hashTable = dict()
    for i in range(1000,10000):
        hashTable[hashlib.sha256(str(i).encode('utf-8')).hexdigest()] = i

    writer = open(output_file_name, 'w')
    for i in range(0,len(inputData)):
        if str(inputData[i][1]) in hashTable.keys():
            writer.write(str(inputData[i][0]) + ',' + str(hashTable[inputData[i][1]]) + '\n')
    writer.close()
