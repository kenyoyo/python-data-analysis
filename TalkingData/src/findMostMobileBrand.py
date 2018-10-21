import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import operator
import plotly.plotly as py
import pygal as pg
import plotly.graph_objs as go
import plotly

plotly.tools.set_credentials_file(username='kendo', api_key='siXULhkZJMZj7uEoCUGo')

data = pd.read_csv('phone_brand_device_model.csv')
brandDict = {}
modelDict = {}
plus = 0
for i in range(5):
    randomList = random.sample(range(37050), 7400)
    np_randomList = np.array(randomList)
    np_randomList += plus
    for j in np_randomList:
        if data.iloc[j]['phone_brand'] in brandDict:
            brandDict[data.iloc[j]['phone_brand']] += 1
        else:
            brandDict[data.iloc[j]['phone_brand']] = 1

        if data.iloc[j]['device_model'] in modelDict:
            modelDict[data.iloc[j]['device_model']] += 1
        else:
            modelDict[data.iloc[j]['device_model']] = 1

    plus += 37050

topTenBrandList = sorted(brandDict.items(), key=operator.itemgetter(1), reverse=True)
topTenModelList = sorted(modelDict.items(), key=operator.itemgetter(1), reverse=True)

print("The most high mobile brand is", topTenBrandList[0][0])
print("The most mobile model is", topTenModelList[0][0])

while(len(topTenBrandList) > 10):
    topTenBrandList.remove(topTenBrandList[len(topTenBrandList)-1])
while(len(topTenModelList) > 10):
    topTenModelList.remove(topTenModelList[len(topTenModelList)-1])

brandList = []
bDataList = []
for bData in topTenBrandList:
    brandList.append(bData[0])
    bDataList.append(bData[1])

modelList = []
mDataList = []
for mData in topTenModelList:
    modelList.append(mData[0])
    mDataList.append(mData[1])

trace = go.Pie(labels=brandList, values=bDataList)
py.iplot([trace], filename='top_brand')
trace = go.Pie(labels=modelList, values=mDataList)
py.iplot([trace], filename='top_model')

'''
plt.pie(bDataList, labels=brandList, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.pie(mDataList, labels=modelList, autopct='%1.1f%%')
plt.show()
'''



