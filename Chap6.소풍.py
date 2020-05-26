# 각 학생들의 쌍에 대해 이들이 서로 친구인지 여부가 주어질 때,
# 학생들을 짝지을 수 있는 방법의 수를 계산하는 함수

#n: 학생의 수, m: 친구 쌍의 수
#friends: 친구인 두 학생의 번호에 대한 정수 쌍

def countPairing(taken, areFriend, n):
    firstFree= -1
    # 남은 학생들 중 가장 번호가 빠른 학생 찾기
    for i in range(n):
        if not taken[i]:
            firstFree=i    

    #기저사례: 모든 taken이 다 True인 경우,
    # 즉 모든 학생이 짝을 찾은 경우 한가지 경우가 만들어짐
    if firstFree == -1 :
        return 1
    
    # 짝지을 학생 결정하기
    ret=0
    for pairWith in range(n):
        if not taken[pairWith] and areFriend[firstFree][pairWith]:
            taken[firstFree]=taken[pairWith]=True
            ret += countPairing(taken, areFriend, n)
            taken[firstFree] = taken[pairWith] = False
    return ret

    tc = int(input())
    for c in range(tc):
        n,m = map(int, input().split())
        list=input()
        list=list.split(' ')
        areFriend=[[False] * 10 for i in range(10)]
        taken = [False] * 10
        for li in range(0, len(list), 2):
            a=int(list[li])
            b=int(list([li+1]))
            areFriend[a][b] = areFriend[b][a] = True

        print(countPairing(taken, areFriend, n))

    


