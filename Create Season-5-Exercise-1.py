import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as inputFile:
        writer = open(output_file_name, 'w')
        reader = csv.reader(inputFile)
        for row in reader:
            name = row[0]
            grade_mean = (float(grade) for grade in row [1:])
            grade_mean = mean(grade_mean)
            out = str(name) + ',' + str(grade_mean) + '\n'
            writer.write(out)
        writer.close()    
    


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as inputFile:
        writer = open(output_file_name, 'w')
        finalList = []
        reader = csv.reader(inputFile)
        for row in reader:
            name = row[0]
            grade_mean = (float(grade) for grade in row [1:])
            grade_mean = mean(grade_mean)
            temp = []
            temp.append(name)
            temp.append(grade_mean)
            finalList.append(temp)
        for i in range(0, len(finalList)):
            for j in range(0, len(finalList)):
                if finalList[i][1] < finalList[j][1]:
                    temp = finalList[i]
                    finalList[i] = finalList[j]
                    finalList[j] = temp
        for i in range(0, len(finalList)-1):
            end = -1
            for j in range(i+1, len(finalList)):
                if finalList[i][1] == finalList[j][1]:
                    end = j
            if end != -1:
                for a in range(i, end + 1):
                    for b in range(i, end + 1):
                        if finalList[a][0] < finalList[b][0]:
                            temp = finalList[a]
                            finalList[a] = finalList[b]
                            finalList[b] = temp

        for i in range(0, len(finalList)):
            out = str(finalList[i][0]) + ',' + str(finalList[i][1]) + '\n'
            writer.write(out)
        writer.close() 
    


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as inputFile:
        writer = open(output_file_name, 'w')
        finalList = []
        reader = csv.reader(inputFile)
        for row in reader:
            name = row[0]
            grade_mean = (float(grade) for grade in row [1:])
            grade_mean = mean(grade_mean)
            temp = []
            temp.append(name)
            temp.append(grade_mean)
            finalList.append(temp)
        for i in range(0, len(finalList)):
            for j in range(0, len(finalList)):
                if finalList[i][1] > finalList[j][1]:
                    temp = finalList[i]
                    finalList[i] = finalList[j]
                    finalList[j] = temp
        for i in range(0, 3):
            out = str(finalList[i][0]) + ',' + str(finalList[i][1]) + '\n'
            writer.write(out)
        writer.close() 
    


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as inputFile:
        writer = open(output_file_name, 'w')
        finalList = []
        reader = csv.reader(inputFile)
        for row in reader:
            name = row[0]
            grade_mean = (float(grade) for grade in row [1:])
            grade_mean = mean(grade_mean)
            temp = []
            temp.append(name)
            temp.append(grade_mean)
            finalList.append(temp)
        for i in range(0, len(finalList)):
            for j in range(0, len(finalList)):
                if finalList[i][1] > finalList[j][1]:
                    temp = finalList[i]
                    finalList[i] = finalList[j]
                    finalList[j] = temp

        out = str(finalList[len(finalList)-1][1]) + '\n'
        writer.write(out)
        out = str(finalList[len(finalList)-2][1]) + '\n'
        writer.write(out)
        out = str(finalList[len(finalList)-3][1]) + '\n'
        writer.write(out)
        writer.close() 
    


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as inputFile:
        writer = open(output_file_name, 'w')
        reader = csv.reader(inputFile)
        sum = 0
        count = 0
        for row in reader:
            grade_mean = (float(grade) for grade in row [1:])
            grade_mean = mean(grade_mean)
            sum += grade_mean
            count += 1

        ave = sum / count
        writer.write(str(ave))
        writer.close() 
