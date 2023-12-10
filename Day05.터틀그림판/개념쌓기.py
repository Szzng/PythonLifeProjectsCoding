import turtle as t


# 함수 정의
def polygon(n):
    for i in range(n):
        t.fd(100)
        t.lt(360 / n)


# 함수 사용
polygon(5)
