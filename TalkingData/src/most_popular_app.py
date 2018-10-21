import csv
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import operator

categoriesDict = {}
unknownList = []
flag = True
with open('label_categories.csv') as myCSV:
    categoriesData = csv.reader(myCSV)
    for row in categoriesData:
        if flag :
            flag = False
            continue
        if(row[1] != '' and row[1] != "unknown"):
            categoriesDict[row[0]] = row[1]
        else:
            unknownList.append(int(row[0]))

appLabelData = pd.read_csv('app_labels.csv')
appEventData = pd.read_csv('app_events.csv')
labelDictionary = {}
plus=0
for i in range(11):
    randomList = random.sample(range(2952097), 10000)    #old 60000
    np_randomList = np.array(randomList)
    np_randomList += plus
    for j in np_randomList:
        getDataApp = appLabelData.loc[appLabelData['app_id'] == appEventData.iloc[j]['app_id']]
        for index, row in getDataApp.iterrows():
             if row[1] in labelDictionary:
                 if appEventData.iloc[j]['is_installed'] == 1:
                     labelDictionary[row[1]][1] += 1
                 if appEventData.iloc[j]['is_active'] == 1:
                     labelDictionary[row[1]][0] += 1
             else:
                labelDictionary[row[1]] = [0, 0]
                if appEventData.iloc[j]['is_installed'] == 1:
                    labelDictionary[row[1]][1] += 1
                if appEventData.iloc[j]['is_active'] == 1:
                    labelDictionary[row[1]][0] += 1
    plus += 2952097

for foundUnknown in unknownList:
    labelDictionary.pop(foundUnknown, None)

topTenApp = sorted(labelDictionary.items(), key=operator.itemgetter(1), reverse=True)
while(len(topTenApp) > 10):
    topTenApp.remove(topTenApp[len(topTenApp)-1])

appLabelList = []
installList = []
activeList = []
for pop in topTenApp:
    appLabelList.append(categoriesDict[str(pop[0])])
    activeList.append(pop[1][0])
    installList.append(pop[1][1])

y_pos = np.arange(len(topTenApp))
plt.barh(y_pos, activeList, 0.35, align='center', alpha=0.5, color='b', label='Active')
plt.barh(y_pos+0.35, installList, 0.35, align='center', alpha=0.5, color='g', label='Install')
plt.yticks(y_pos+0.35, appLabelList)
plt.xlabel("Frequency")
plt.ylabel("Active and install")
plt.title("Top 10 most poppular mobile application categories")
plt.legend()
plt.show()



