import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode

def calculateThisDay(thatDay) :
    if(thatDay[5:7] != "01"):
        if(thatDay[5:7] == "02"):
            return (int(thatDay[8:10]) + 31) % 7
        if (thatDay[5:7] == "03"):
            return (int(thatDay[8:10]) + 60) % 7
        if (thatDay[5:7] == "04"):
            return (int(thatDay[8:10]) + 91) % 7
        if (thatDay[5:7] == "05"):
            return (int(thatDay[8:10]) + 121) % 7
        if (thatDay[5:7] == "06"):
            return (int(thatDay[8:10]) + 152) % 7
        if (thatDay[5:7] == "07"):
            return (int(thatDay[8:10]) + 182) % 7
        if (thatDay[5:7] == "08"):
            return (int(thatDay[8:10]) + 213) % 7
        if (thatDay[5:7] == "09"):
            return (int(thatDay[8:10]) + 244) % 7
        if (thatDay[5:7] == "10"):
            return (int(thatDay[8:10]) + 274) % 7
        if (thatDay[5:7] == "11"):
            return (int(thatDay[8:10]) + 305) % 7
        if (thatDay[5:7] == "12"):
            return (int(thatDay[8:10]) + 335) % 7
    else:
        return int(thatDay[8:10]) % 7

mostTimeInterval = []
mostDayPerUse = []

data = pd.read_csv('events.csv')
plus=0

for i in range(50):
    randomLsit = random.sample(range(65059), 1300)
    np_randomList = np.array(randomLsit)
    np_randomList += plus
    for j in np_randomList:
        mostTimeInterval.append(int(data.iloc[j]['timestamp'][11:13]))
        mostDayPerUse.append(calculateThisDay(data.iloc[j]['timestamp'][0:10]))
    plus += 65059

tick_labTime = ["12pm", "01pm", "02pm", "03pm", "04pm", "05pm", "06am",
             "07am", "08am", "09am", "10am", "11am", "12am", "01am",
             "02am", "03am", "04am", "05am", "06pm", "07pm", "08pm",
             "09pm", "10pm", "11pm"]
tick_valueTime = np.arange(24)
tick_labDay = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
tick_valueDay = np.arange(7)

print("Most begin time is", tick_labTime[mode(mostTimeInterval)])
print("Most day is", tick_labDay[mode(mostDayPerUse)])

plt.figure(1)
plt.title("Most begin time did user use app")
plt.xlabel("Begin time of day")
plt.ylabel("Frequency")
plt.xticks(tick_valueTime, tick_labTime)
plt.hist(mostTimeInterval, edgecolor='black', bins=np.arange(25), align='left')
plt.show()

plt.figure(2)
plt.title("Most day did user use app")
plt.xlabel("day of the week")
plt.ylabel("Frequency")
plt.xticks(tick_valueDay, tick_labDay)
plt.hist(mostDayPerUse, edgecolor='black', bins=np.arange(8), align='left')
plt.show()