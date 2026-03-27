import pandas as pd
Students = pd.DataFrame(columns=["Name", "Score", "Grade"])

Average = 0
Max = 0
Min = 0

def AddStudent(Name, Score):
    Letter = ""
    if (Score >= 90): Letter = "A"
    elif (Score >= 80): Letter = "B"
    elif (Score >= 70): Letter = "C"
    elif (Score >= 60): Letter = "D"
    else: Letter = "F"

    row = [Name, Score, Letter]
    Students.loc[len(Students)] = row
    Average, Min, Max = __UpdateScore()

def __UpdateScore():
    tSum = 0
    tMin = 999
    tMax = 0
    rowNum = 0
    for index, row in Students.iterrows():
        tSum += row["Score"]
        if (row["Score"] < tMin):
            tMin = row["Score"]
        if (row["Score"] > tMax):
            tMax = row["Score"]
        rowNum += 1
    return (tSum / rowNum, tMin, tMax)
    



AddStudent("bob", 85)
AddStudent("cam", 40)
print(Average)
        


