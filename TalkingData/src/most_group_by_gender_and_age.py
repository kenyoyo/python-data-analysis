import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

data = pd.read_csv('gender_age_train.csv')

currentMaxGroupTotal = -sys.maxsize
mostGroup = None

groupDict = {}
for index, row in data.iterrows():
    isNewFoundGroup = True
    for dict in groupDict:
        if(row[3] == dict):
            groupDict[row[3]] += 1
            isNewFoundGroup = False

            if groupDict[row[3]] > currentMaxGroupTotal:
                currentMaxGroupTotal = groupDict[row[3]]
                mostGroup = dict
            break
    if isNewFoundGroup:
        groupDict[row[3]] = 1;

print("most group of user is", mostGroup)

groupList =[]
tick_labGroup = []
i=0
for dict in groupDict:
    for j in range(groupDict[dict]):
        groupList.append(i)
    tick_labGroup.append(dict)
    i+=1

plt.title("Total user use phone group by gender and age")
plt.xlabel("gender and age")
plt.ylabel("Frequency")
tick_valueGroup = np.arange(11)
plt.hist(groupList, bins=np.arange(12), edgecolor='black', align='left')
plt.xticks(tick_valueGroup, tick_labGroup)
plt.show()
