import pandas as pd
import random
import numpy as np
import math


userData = pd.read_csv('gender_age_train.csv')
eventData = pd.read_csv('events.csv')
appEventData = pd.read_csv('app_events.csv')
appLabelData = pd.read_csv('app_labels.csv')
phoneData = pd.read_csv('phone_brand_device_model.csv')
categoriesData = pd.read_csv('label_categories.csv')

#sampling = np.arange(1000) #32473067
split = math.floor(eventData.shape[0] / 5)
#split = math.floor(len(sampling)/5)

for cross in range(5):
    predictStartIdx = cross * split
    predictEndIdx = predictStartIdx + split
    runIdx = 0

    appInformationProbe = {}
    timeStampProbe = {}
    longitudeProbe = {}
    latitudeProbe = {}
    #phoneBrandProbe = {}
    #deviceModelProbe = {}
    classGroupProbe = {}

    for index, row in eventData.iterrows():
        if(predictStartIdx <= runIdx <= predictEndIdx):
            runIdx += 1
            continue

        getDeviceId = row[1]

        if userData.loc[userData['device_id'] == getDeviceId].empty:
            continue
        getGroup = userData.loc[userData['device_id'] == getDeviceId].iloc[0]['group']

        '''getPhoneByDeviceId = phoneData.loc[phoneData['device_id'] == getDeviceId]
        if getPhoneByDeviceId.empty:
            continue
        for index2, row2 in getPhoneByDeviceId.iterrows():
            getPhoneBrand = row2[1]
            getDeviceModel = row2[2]

            if getPhoneBrand in phoneBrandProbe:
                if getGroup in phoneBrandProbe[getPhoneBrand]:
                    phoneBrandProbe[getPhoneBrand][getGroup] += 1
                else:
                    phoneBrandProbe[getPhoneBrand][getGroup] = 1
            else:
                phoneBrandProbe[getPhoneBrand] = {}
                phoneBrandProbe[getPhoneBrand][getGroup] = 1

            if getDeviceModel in deviceModelProbe:
                if getGroup in deviceModelProbe[getDeviceModel]:
                    deviceModelProbe[getDeviceModel][getGroup] += 1
                else:
                    deviceModelProbe[getDeviceModel][getGroup] = 1
            else:
                deviceModelProbe[getDeviceModel] = {}
                deviceModelProbe[getDeviceModel][getGroup] = 1'''

        getEventByDeviceId = eventData.loc[eventData['device_id'] == getDeviceId]
        if getEventByDeviceId.empty:
            continue
        for index2, row2 in getEventByDeviceId.iterrows():
            getTimestamp = row2[2]
            getLatitude = row2[3]
            getLongitude = row2[4]
            getAppEventByEventId = appEventData.loc[appEventData['event_id'] == row2[1]]
            if getAppEventByEventId.empty:
                continue
            for index3, row3 in getAppEventByEventId.iterrows():
                getIsInstall = row3[2]
                getIsActive = row3[3]
                getAppId = row3[1]

                if getAppId in appInformationProbe:
                        if getIsInstall:
                            if getGroup in appInformationProbe[getAppId]['isInstalled']:
                                appInformationProbe[getAppId]['isInstalled'][getGroup] += 1
                            else:
                                appInformationProbe[getAppId]['isInstalled'][getGroup] = 1
                        else:
                            if getGroup in appInformationProbe[getAppId]['notInstalled']:
                                appInformationProbe[getAppId]['notInstalled'][getGroup] += 1
                            else:
                                appInformationProbe[getAppId]['notInstalled'][getGroup] = 1

                        if getIsActive:
                            if getGroup in appInformationProbe[getAppId]['isActive']:
                                appInformationProbe[getAppId]['isActive'][getGroup] += 1
                            else:
                                appInformationProbe[getAppId]['isActive'][getGroup] = 1
                        else:
                            if getGroup in appInformationProbe[getAppId]['notActive']:
                                appInformationProbe[getAppId]['notActive'][getGroup] += 1
                            else:
                                appInformationProbe[getAppId]['notActive'][getGroup] = 1
                else:
                    appInformationProbe[getAppId] = {
                                                     'isInstalled': {},
                                                     'isActive': {},
                                                     'notInstalled': {},
                                                     'notActive': {}
                                                    }
                    if getIsInstall:
                        appInformationProbe[getAppId]['isInstalled'][getGroup] = 1
                        appInformationProbe[getAppId]['notInstalled'][getGroup] = 0
                    else:
                        appInformationProbe[getAppId]['notInstalled'][getGroup] = 1
                        appInformationProbe[getAppId]['isInstalled'][getGroup] = 0

                    if getIsActive:
                        appInformationProbe[getAppId]['isActive'][getGroup] = 1
                        appInformationProbe[getAppId]['notActive'][getGroup] = 0
                    else:
                        appInformationProbe[getAppId]['notActive'][getGroup] = 1
                        appInformationProbe[getAppId]['isActive'][getGroup] = 0

                if getGroup in classGroupProbe:
                    classGroupProbe[getGroup] += 1
                else:
                    classGroupProbe[getGroup] = 1

                if getTimestamp in timeStampProbe:
                    if getGroup in timeStampProbe[getTimestamp]:
                        timeStampProbe[getTimestamp][getGroup] += 1
                    else:
                        timeStampProbe[getTimestamp][getGroup] = 1
                else:
                    timeStampProbe[getTimestamp] = {}
                    timeStampProbe[getTimestamp][getGroup] = 1

                if getLongitude in longitudeProbe:
                    if getGroup in longitudeProbe[getLongitude]:
                        longitudeProbe[getLongitude][getGroup] += 1
                    else:
                        longitudeProbe[getLongitude][getGroup] = 1
                else:
                    longitudeProbe[getLongitude] = {}
                    longitudeProbe[getLongitude][getGroup] = 1

                if getLatitude in latitudeProbe:
                    if getGroup in latitudeProbe[getLatitude]:
                        latitudeProbe[getLatitude][getGroup] += 1
                    else:
                        latitudeProbe[getLatitude][getGroup] = 1
                else:
                    latitudeProbe[getLatitude] = {}
                    latitudeProbe[getLatitude][getGroup] = 1
        runIdx += 1

    print(classGroupProbe)
    print(timeStampProbe)
    print(longitudeProbe)
    print(latitudeProbe)
    #print(phoneBrandProbe)
    #print(deviceModelProbe)
    print(appInformationProbe)

    for timestamp in timeStampProbe:
        for isGroup in timeStampProbe[timestamp]:
            if timeStampProbe[timeStampProbe][isGroup] == 0:
                timeStampProbe[timeStampProbe][isGroup] = 1
            timeStampProbe[timestamp][isGroup] = timeStampProbe[timestamp][isGroup] / classGroupProbe[isGroup]

    for longitude in longitudeProbe:
        for isGroup in longitudeProbe[longitude]:
            if longitudeProbe[longitude][isGroup] == 0:
                longitudeProbe[longitudeProbe][isGroup] = 1
            longitudeProbe[longitude][isGroup] = longitudeProbe[longitude][isGroup] / classGroupProbe[isGroup]

    for latitude in latitudeProbe:
        for isGroup in latitudeProbe[latitude]:
            if latitudeProbe[latitude][isGroup] == 0:
                latitudeProbe[latitude][isGroup] = 1
            latitudeProbe[latitude][isGroup] = latitudeProbe[latitude][isGroup] / classGroupProbe[isGroup]

    '''for brand in phoneBrandProbe:
        for isGroup in phoneBrandProbe[brand]:
            phoneBrandProbe[brand][isGroup] = phoneBrandProbe[brand][isGroup] / classGroupProbe[isGroup]'''

    '''for model in deviceModelProbe:
        for isGroup in deviceModelProbe[model]:
            deviceModelProbe[model][isGroup] = deviceModelProbe[model][isGroup] / classGroupProbe[isGroup]'''

    for appId in appInformationProbe:
        for appStatus in appInformationProbe[appId]:
            for isGroup in appInformationProbe[appId][appStatus]:
                if appInformationProbe[appId][appStatus][isGroup] == 0:
                    appInformationProbe[appId][appStatus][isGroup] = 1
                appInformationProbe[appId][appStatus][isGroup] = appInformationProbe[appId][appStatus][isGroup] / classGroupProbe[isGroup]

    for group in classGroupProbe:
        classGroupProbe[group] = classGroupProbe[group] / sum(classGroupProbe.values())

    print(classGroupProbe)
    print(timeStampProbe)
    print(longitudeProbe)
    print(latitudeProbe)
    #print(phoneBrandProbe)
    #print(deviceModelProbe)
    print(appInformationProbe)

    for predictIdx in range(predictStartIdx, predictEndIdx+1):
        predictResult = list[0] * len(classGroupProbe)
        predictResult = np.array(predictResult)
        getPredictDeviceId = eventData.iloc[predictIdx]['device_id']
        print("Actual gender is", userData.loc[userData['device_id'] == getPredictDeviceId])
        count = 0

        getEventByDeviceId = eventData.loc[eventData['device_id'] == getPredictDeviceId]
        if getEventByDeviceId.empty :
            continue

        for index, row in getEventByDeviceId.iterrows():
            getTimestamp = row[2]
            getLongitude = row[3]
            getLatitude = row[4]
            getAppEventByEventId = appEventData.loc['event_id' == getEventByDeviceId]
            if getAppEventByEventId.empty :
                continue
            for index2, row2 in getAppEventByEventId.iterrows():
                predictList = []
                getAppId = row2[1]
                getIsInstall = row2[2]
                getIsActive = row2[3]

                if getIsInstall:
                    getIsInstall = appInformationProbe[getAppId]['isInstalled']
                else:
                    getIsInstall = appInformationProbe[getAppId]['notInstalled']

                if getIsActive:
                    getIsActive = appInformationProbe[getAppId]['isActive']
                else:
                    getIsActive = appInformationProbe[getAppId]['notActive']

                for getGroup in classGroupProbe:
                    predictTemp = timeStampProbe[getTimestamp][getGroup] * longitudeProbe[getLongitude][getGroup] * latitudeProbe[getLatitude][getGroup] * getIsInstall[getGroup] * getIsActive[getGroup] * classGroupProbe[getGroup]
                    predictList.append(predictTemp)

                predictList = np.array(predictList)
                predictResult += predictList
                count += 1

        predictResult /= count
        print("Predict gender is")
        count = 0
        for key in classGroupProbe:
            print(key, ": ", predictResult[count])
            count += 1






