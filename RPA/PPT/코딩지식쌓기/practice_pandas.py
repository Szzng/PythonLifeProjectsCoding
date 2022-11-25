import pandas as pd

# 엑셀파일 읽어오기
data = pd.read_excel('졸업생목록.xlsx')

# 표의 세로 열을 기준으로 데이터 저장하기
students = data['졸업생']
birthdays = data['생일']
classes = data['반']

# 반복문을 이용해 차례대로 출력해보기
for i in range(len(data)):
    print('='*3, i+1, '번째 반복', '='*3)
    print('졸업생:', students[i])
    print('생일:', birthdays[i])
    print('반:', classes[i])

# 참고 : data, students, birthdays, classes 출력해보기
print(data)
print(students)
print(birthdays)
print(classes)