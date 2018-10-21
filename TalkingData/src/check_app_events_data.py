#not found invalid data in all row
#total data instance is complete

import csv

with open('app_events.csv') as myCSV:
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

        #found invalid is_install and is_active data each default by one because column
        if(row[2] != '0' and row[2] != '1'):
            print("found invalid is_install data")
        if (row[3] != '0' and row[3] != '1'):
            print("found invalid is_active data")

    print("total data instance: ", count)