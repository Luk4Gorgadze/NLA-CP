import numpy as np

# CALCULATE FROBENIUS NORM
def fro(Matrix,rowNum,colNum):
    frobenius = 0    
    for i in range(rowNum):
        for j in range(colNum):
            frobenius += abs(Matrix[i][j]) ** (2)
    frobenius **= (1./2)
    return frobenius

studentList = {}

rowNum = 4
colNum = 5
for i in range(20):
    student = np.random.randint(50, size=(rowNum, colNum))
    studentList.update({i: (student, fro(student,rowNum,colNum))})


def rankStudent():
    return dict(sorted(studentList.items(), key=lambda item: fro(item[1][0],rowNum,colNum)))


res = rankStudent()
for key, value in res.items():
    print('Student id:', key)
    print(value[0])
    print("Student's frobenius norm", value[1])
    print('------------------')
