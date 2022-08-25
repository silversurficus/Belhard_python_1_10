"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import csv
def max_delta():
    percent = []
    reader = csv.reader(open('world_population.csv', 'r'))
    for row in reader:
        percent.append(row[2])
    maximum = max(percent[1:])
    reader = csv.reader(open('world_population.csv', 'r'))
    for row in reader:
        if maximum == row[2]:
            return row[0]

print(max_delta())