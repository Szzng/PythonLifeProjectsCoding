import random

number = random.randint(1, 100)

while True:
    answer = int(input('내가 고른 숫자를 맞춰 봐!'))

    if answer == number:
        print('제법이군! 정답이야!')
        break

    elif answer < number:
        print('업 Up!')

    else:
        print('다운 Down!')
