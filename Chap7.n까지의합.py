# n까지의 합을 분할 정복으로 계산하기
# -> 1부터 n까지의 합을 n조각으로 나눈 뒤 반으로 잘라 n/2개로 이루어진 부분 문제로 본다

def fastsum(n):
    if n ==1:    # 기저사례
        return 1
    if n % 2 == 1:
        return fastsum(n-1)+n
    return fastsum(n/2)*2 + (n/2) * (n/2)


print(fastsum(5))
print(fastsum(6))