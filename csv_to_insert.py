#!/usr/bin/python
import csv

with open('res/people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    with open('insert.sql', 'w') as writer:
        for row in reader:
            writer.write('INSERT INTO Persons VALUES (' + row[0] + ',"' + row[1] + '","' + row[2] + '","' + row[3] + '","' + row[4] + '");\n')
            print('INSERT INTO Persons VALUES (' + row[0] + ',"' + row[1] + '","' + row[2] + '","' + row[3] + '","' + row[4] + '")')
