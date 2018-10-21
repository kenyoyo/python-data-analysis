import sys
import csv

#total of information that we have
unknownModel = 185245

currentHighModel = -sys.maxsize
currentSecondModel = -sys.maxsize
currentThirdModel = -sys.maxsize


modelList = []

with open("phone_brand_device_model.csv", encoding='utf8') as myCSV:
    csvReader = csv.reader(myCSV)
    for row in csvReader:
        isNewModel = True   #to check the data that we take in is newbrand to create new information
        for knowModel in modelList:
            if knowModel["modelName"] == row[2]:   #check if is knowbrand we don't need to create new information about it but plus this amount
                knowModel["amount"] += 1
                isNewModel = False
                if currentHighModel < knowModel["amount"]:      #update currentHighBrand
                    currentHighModel = knowModel["amount"]
                    knowHighModel = knowModel["modelName"]
                elif currentSecondModel < knowModel["amount"]:
                    currentSecondModel = knowModel["amount"]
                    knowSecondModel = knowModel["modelName"]
                elif currentThirdModel < knowModel["amount"]:
                    currentThirdModel = knowModel["amount"]
                    knowThirdModel = knowModel["modelName"]
                break

        if isNewModel:    #create new brand put in brandList
            newBrand = {
                "modelName" : row[2],
                "amount" : 1
            }
            modelList.append(newBrand)
        unknownModel -= 1   #reduce unknownBrand

        if currentThirdModel > unknownModel:     #if currentHighBrand is > unknowBrand that we have answer for most mobile brand
            print("The most high mobile model is", knowHighModel)
            print("The most second mobile model is", knowSecondModel)
            print("The most third mobile model is", knowThirdModel)
            break



