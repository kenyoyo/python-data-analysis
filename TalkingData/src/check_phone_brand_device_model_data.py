#not found invalid data in all row
#total data instance is complete

import csv

with open('phone_brand_device_model.csv', encoding='utf8') as myCSV:
    csvReader = csv.reader(myCSV)

    count = -1
    for row in csvReader:
        count = count+1
        if(row[0] == '' or row[0] == "unknown"):
            print("found invalid data")
        if (row[1] == '' or row[1] == "unknown"):
            print("found invalid data")
        if (row[2] == '' or row[2] == "unknown"):
            print("found invalid data")

    print("total data instance: ", count)
