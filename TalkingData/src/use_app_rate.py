import pandas as pd
import random
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import mean

data = pd.read_csv('events.csv')

plus=0

def calculateGrowthRate(value):
    ratePerDay = []
    for i in range(6):
        growthPercent = (value[i+1] - value[i]) * 100 / value[i]
        ratePerDay.append(growthPercent)
    return mean(ratePerDay)

perDayList = []
for week in range(8):
    perDayList.append(0)

'''def whatWeekOfDay(thisDay):
    splitInformation = thisDay.split('-')
    sep = [int(s) for s in splitInformation]
    print(sep)
    return datetime.date(sep[0], sep[1], sep[2]).isocalendar()[1]'''

for i in range(50):
    randomLsit = random.sample(range(65059), 1300)
    np_randomList = np.array(randomLsit)
    np_randomList += plus
    for j in np_randomList:
        temp = int(data.iloc[j]['timestamp'][8:10])
        if temp <= 7:
            perDayList[temp] += 1
    plus += 65059

perDayList.remove(0)

'''tick_labWeek = ["week1", "week2", "week3", "week4", "week5", "week6", "week7"
               "week8", "week9", "week10", "week11", "week12","week13", "week14"
               "week15", "week16", "week17", "week18", "week19","week20", "week21"
               "week22", "week23", "week24", "week25", "week26", "week27", "week28"
               "week29", "week30", "week31", "week32", "week33","week34", "week35"
               "week36", "week37", "week38", "week39", "week40","week41", "week42"
               "week43", "week44", "week45", "week46", "week47","week48", "week49"
               "week50", "week51", "week52"]'''

print("The mean of Growth rate is",calculateGrowthRate(perDayList))
plt.plot(np.arange(7)+1, perDayList)
plt.title("Growth line of use app between 1/6/2560 - 7/6/2560")
plt.xlabel("day")
plt.ylabel("total app use by user")
plt.show()