import pandas as pd

# 엑셀파일 읽어오기
data = pd.read_excel('학생목록.xlsx')

# 표의 세로 열을 기준으로 데이터 저장하기
names = data['이름']
grades = data['학년']
classes = data['반']

# 반복문을 이용해 차례대로 출력해보기
for i in range(len(data)):
    print('=' * 3, i + 1, '번째 반복', '=' * 3)
    print('이름:', names[i])
    print('학년:', grades[i])
    print('반:', classes[i])

# 참고 : data, names, grades, classes 출력해보기
print(data)
print(names)
print(grades)
print(classes)
