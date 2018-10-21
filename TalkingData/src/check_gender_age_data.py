#not found invalid or unknown data in all row
#not found invalid gender data in all row
#total data instance is complete
#group column data is have many format to tell about this data

import csv
import sys

with open('gender_age_train.csv') as myCSV:
    csvReader = csv.reader(myCSV)
    findMaxAge = -sys.maxsize
    findMinAge = sys.maxsize
    userAge = None

    count=-1
    for row in csvReader:
        count = count+1

        if row[2].isdigit():
            userAge = int(row[2])

        #check invalid and unknown data
        if(row[0] == "unknown" or row[0] == ''):
            print("found invalid data")
        if(row[1] == "unknown" or row[1] == ''):
            print("found invalid data")
        if(row[2] == "unknown" or row[2] == ''):
            print("found invalid data")
        if(row[3] == "unknown" or row[3] == ''):
            print("found invalid data")

        #find min and max of user age
        if userAge != None:
            if(userAge > findMaxAge):
                findMaxAge=userAge
            if(userAge < findMinAge):
                findMinAge=userAge

        #find invalid gender data have 1 default because column "gender"
        if row[1] != "M" and row[1] != "F":
            print("found invalid gender data")

    print("total data instance: ", count)
    print("maximum and minimum age of user is:", findMaxAge, "and", findMinAge)

            
