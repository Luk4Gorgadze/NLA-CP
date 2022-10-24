from matplotlib import pyplot as plt
import numpy as np
import random

def norm3(vec):
    res = 0
    for el in vec:
        res += pow(el,3)
    res = res ** (1./3)
    return res


studentList = {}
random.seed(20)
for i in range(225):
    English = random.randint(120,200)
    Georgian = random.randint(120,200)
    Math = random.randint(120,200)
    student = np.array([English,Georgian,Math])
    studentList.update({i:(student, norm3(student))})


def rankStudent():
    return dict(sorted(studentList.items(), key=lambda item: item[1][1]))

def groupByLevels(rankedStudents):
    studs = list(rankedStudents.values())
    levels = {}
    for i in range(15):
        levels.update({i:[]})
    for i in range(15):
        for j in range(15):
            l = levels[i]
            l.append(studs.pop())
            levels.update({i:l})
    return levels



def backTrace(leveledStudents,avgSum,levelIndex,currSum,currentList):
    # Base case
    if(len(currentList) == 15):
        if(abs(currSum - avgSum) < 1000):
            return True
        else:
            return False

    List = leveledStudents[levelIndex].copy()
    for index,stud in enumerate(List):
        currSum += stud[1]
        sstud = ((levelIndex,index),stud)
        currentList.append(sstud)

        if currSum > avgSum:
            currSum -= stud[1]
            currentList.remove(sstud)
            return False

        if backTrace(leveledStudents,avgSum,levelIndex+1,currSum,currentList):  
            return True
        else:
            currSum -= stud[1]
            currentList.remove(sstud)
            continue


def partition(leveledStudents,avgSum,levelIndex,currSum):
    #  Choose member from each list Recursively
    lStudents = leveledStudents.copy()
    groups = {}
    for i in range(15):
        currentList = []
        backTrace(leveledStudents,avgSum,levelIndex,currSum,currentList)
        groups.update({i:currentList})
        for index,v in enumerate(currentList):
            print("V", v)
            print("V only tuple",v[1])
            l = lStudents[14-index]
            l.pop(v[0][1])
            lStudents[14 - index] = l
            print("end")
    
    return groups


res = rankStudent()
leveledStuds = groupByLevels(res)

sum = 0
for k,v in studentList.items():
    sum += v[1]
avgSum = sum / 15.0

group = partition(leveledStuds,avgSum + 40,0,0)
scores = []
for k,v in group.items():
    print(k)
    print(v)
    score = 0
    for el in v:
        score += el[1][1]
    scores.append(score)


labels = list(map(lambda k: k,group.keys()))
sizes = scores

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal') 

plt.show()



