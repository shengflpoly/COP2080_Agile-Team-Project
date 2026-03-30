import pandas as pd
__Students = pd.DataFrame(columns=["Name", "Score", "Grade"])
__Average = 0
__Max = 0
__Min = 0

def __UpdateScore():
    tSum = 0
    tMin = 999
    tMax = 0
    rowNum = 0
    for index, row in __Students.iterrows():
        tSum += row["Score"]
        if (row["Score"] < tMin):
            tMin = row["Score"]
        if (row["Score"] > tMax):
            tMax = row["Score"]
        rowNum += 1
    return (tSum / rowNum, tMin, tMax)

def AddStudent(Name, Score):
    Letter = ""
    if (Score >= 90): Letter = "A"
    elif (Score >= 80): Letter = "B"
    elif (Score >= 70): Letter = "C"
    elif (Score >= 60): Letter = "D"
    else: Letter = "F"

    row = [Name, Score, Letter]
    __Students.loc[len(__Students)] = row

    global __Average, __Min, __Max
    (__Average, __Min, __Max) = __UpdateScore()

def GetDataframe():
    return __Students

def GetMin():
    return __Min

def GetMax():
    return __Max

def GetAverage():
    return __Average
