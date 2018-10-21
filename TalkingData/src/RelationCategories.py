import pandas as pd
import random
import numpy as np
import statistics
import itertools

def generateItemSet(itemSet, k):
    genList = []
    flag = True
    if k == 0:
        for i in range(len(itemSet)-1):
            for j in range(i+1, len(itemSet)):
                genList.append(itemSet[i] + ',' + itemSet[j])
    else:
        for i in range(len(itemSet) - 1):
            for j in range(i+1, len(itemSet)):
                match1 = itemSet[i].split(',')
                match2 = itemSet[j].split(',')
                for m in range(len(match1) - 1):
                    if match1[m] == match2[m]:
                        flag = True
                    else:
                        flag = False
                        break;

                if flag:
                    genList.append(itemSet[i] + "," + match2[len(match2)-1])

    return genList

def checkSupport(itemSet):
    tempItemSet = []
    for i in itemSet:
        tempItemSet.append(i)
    for i in tempItemSet:
        tempSplitItem = i.split(',')
        tempIntersect = appIdinCategoriesDict[tempSplitItem[0]]
        for j in tempSplitItem:
            tempIntersect = set(tempIntersect) & set(appIdinCategoriesDict[j])
        if len(tempIntersect) / len(foundAppIdList) < minSupport:
            itemSet.remove(i)
        else:
            supportCategoriesAppList.append(i)
            supportCategoriesValueList.append(len(tempIntersect) / len(foundAppIdList))
            supportCategoriesSizeList.append(len(tempSplitItem))
            supportCategoriesDict[i] = len(tempIntersect) / len(foundAppIdList)

    return itemSet

def calculateConfidentAndLift(LHS, RHS):
    composite = LHS + "," + RHS
    numLHS = 0
    for i in LHS:
        numLHS += ord(i)

    numRHS = 0
    for i in RHS:
        numRHS += ord(i)

    numComposite = 0
    for i in composite:
        numComposite += ord(i)

    for category in supportCategoriesDict:
        matchNum = 0
        for i in category:
            matchNum += ord(i)
        if matchNum == numLHS:
            supLHS = supportCategoriesDict[category]
        if matchNum == numRHS:
            supRHS = supportCategoriesDict[category]
        if matchNum == numComposite:
            supComposite = supportCategoriesDict[category]

    return [supComposite / supLHS, supComposite / supLHS * supRHS]

minSupport = 0.2
appLabelData = pd.read_csv('app_labels.csv')
labelCategoriesData = pd.read_csv('label_categories.csv')

appIdinCategoriesDict = {}
foundAppIdList = []

sampling = random.sample(range(459943), 2500)
for samp in sampling:
    appId = appLabelData.iloc[samp]['app_id']
    if appId in foundAppIdList:
        continue
    else:
        foundAppIdList.append(appId)
        appLabels = appLabelData.loc[appLabelData['app_id'] == appId]
        for index, row in appLabels.iterrows():
            appCategories = labelCategoriesData.loc[labelCategoriesData['label_id'] == row[1]].iloc[0]['category']
            if appCategories in appIdinCategoriesDict:
                appIdinCategoriesDict[appCategories].append(appId)
            else:
                appIdinCategoriesDict[appCategories] = []
                appIdinCategoriesDict[appCategories].append(appId)

L = [[]]
supportCategoriesDict = {}
supportCategoriesAppList = []
supportCategoriesValueList = []
supportCategoriesSizeList = []
for category in appIdinCategoriesDict:
    if len(appIdinCategoriesDict[category]) / len(foundAppIdList) > minSupport:
        supportCategoriesAppList.append(category)
        supportCategoriesValueList.append(len(appIdinCategoriesDict[category]) / len(foundAppIdList))
        supportCategoriesSizeList.append(1)
        supportCategoriesDict[category] = len(appIdinCategoriesDict[category]) / len(foundAppIdList)
        L[0].append(category)

k=1
while len(L[k-1]) != 0:
    C = generateItemSet(L[k-1], k-1)
    L.append(checkSupport(C))
    k+=1

print(L)
print(supportCategoriesDict)

associationList = []
confidenceList = []
liftList = []
for i in range(1, len(L)-1):
    for j in L[i]:
        data = j.split(',')
        for k in range(1, i+1):
            for k1 in itertools.combinations(data, k):
                LHS = []
                RHS = []
                for category in k1:
                    LHS.append(category)

                for category in data:
                    if category not in LHS:
                        RHS.append(category)

                LHS = ','.join(LHS)
                RHS = ','.join(RHS)
                answer = calculateConfidentAndLift(LHS, RHS)
                associationList.append(LHS + " => " + RHS)
                confidenceList.append(answer[0])
                liftList.append(answer[1])


associationDataframe = {
                            "No." : list(range(1, len(associationList)+1)),
                            "Association Rules" : associationList,
                            "Confidence" : confidenceList,
                            "Lift" : liftList
                        }

pdf = pd.DataFrame.from_dict(associationDataframe)
pdf = pdf[["No.", "Association Rules", "Confidence", "Lift"]]
pdf.to_csv("application_relation.csv")
print(pdf)

print(len(supportCategoriesDict))

supportDataframe = {
                        "No." : list(range(1, len(supportCategoriesAppList)+1)),
                        "Application" : supportCategoriesAppList,
                        "Support" : supportCategoriesValueList,
                        "Size" : supportCategoriesSizeList
                    }

sdf = pd.DataFrame.from_dict(supportDataframe)
sdf = sdf[["No.", "Application", "Support", "Size"]]
sdf.to_csv("support_value.csv")
print(sdf)