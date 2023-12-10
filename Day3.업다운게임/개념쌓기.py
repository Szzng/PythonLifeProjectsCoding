while True:
    answer = input('숫자를 입력하세요. 종료는 q를 입력하세요.')

    if answer == 'q':
        print('프로그램을 종료합니다.')
        break
    elif int(answer)%2 == 1:
        print('홀수!')
    else:
        print('짝수!')
