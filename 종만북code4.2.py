## 반복문 수행 횟수가 N이 되도록 이동 평균 구하기

# M-이동평균: 최근 M일간의 평균으로 정의.
# 이동평균 정의에 따르면-> 각 이동평균은 M일간의 값의 합을 M으로 나누어 구함.
# 수행 횟수 줄이기 -> M-1에 구했던 값의 합에서 0일째의 값을 빼고 M일째의 값을 더해서 구함!

def movingAverage(numarray, M) :
    n= len(numarray)
    partialsum = 0
    for i in range(M-1):
        partialsum += numarray[i]
    MA=[]
    for i in range(M-1, len(numarray)):
        partialsum += numarray[M-1]
        MA.append(partialsum/3)
        partialsum -= numarray[i-M+1]

    return MA

print(movingAverage([13,2,23,25,19,14,36,13,17], 3))

