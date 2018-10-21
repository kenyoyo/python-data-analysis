#not found invalid data at row[0] but unknown and null data in some row[1]
#total data instance is complete

import csv

with open('label_categories.csv') as myCSV:
    print("-----check label_categories.csv-----")
    csvReader = csv.reader(myCSV)
    count=-1
    for row in csvReader:
        count = count+1
        if(row[0] == "unknown" or row[0] == ' '):
            print("found invalid data")
        if(row[1] == ''):
            print("null information at id", row[0])
        if(row[1] == "unknown"):
            print("unknow category at id ", row[0])

    print("total data instance: ", count)