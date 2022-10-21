import numpy as np

studentList = {}

for i in range(20):
    student = np.random.randint(50, size=(4, 5))
    studentList.update({i:(student, np.linalg.norm(student,ord='fro'))})

def rankStudent():
    return dict(sorted(studentList.items(), key=lambda item: np.linalg.norm(item[1][0],ord='fro')))

res = rankStudent()
for key,value in res.items():
    print('Student id:',key)
    print(value[0])
    print("Student's frobenius norm",value[1])
    print('------------------')

