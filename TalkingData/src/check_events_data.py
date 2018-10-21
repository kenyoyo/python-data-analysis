#not found invalid data in all row but some zero point at latitude and longtitude
#total data instance is complete

import csv

with open('events.csv') as myCSV:
    csvReader = csv.reader(myCSV)
    count=-1
    for row in csvReader:
        count=count+1
        if(row[0] == "unknown" or row[0] == ''):
            print("found invalid data")
        if(row[1] == "unknown" or row[1] == ''):
            print("found invalid data")
        if(row[2] == "unknown" or row[2] == ''):
            print("found invalid data")
        if(row[3] == "unknown" or row[3] == ''):
            print("found invalid data")
        if(row[4] == "unknown" or row[4] == ''):
            print("found invalid data")

    print("total data instance: ", count)