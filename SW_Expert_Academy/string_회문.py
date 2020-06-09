### 뭐가 문제인지 잘 모르겠음 ㅠㅠㅠㅠㅠ


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    words=[]
    
    ## 가로 확인
    for row in range(N):
        words.append(input())
        for i in range(N-M+1):
            if words[row][i:i+M] == words[row][i:i+M][::-1]:
            	ret=words[row][i:i+M]

    ## 세로 확인
    # 세로용 데이터 만들기
    word2=[]
    for i in range(N):
        sub=''
        for j in range(N):
            sub= sub + words[i][j]
        word2.append(sub)
    #세로에서 같은글자 확인하기
    for col in range(N):
        for i in range(N-M+1):
            if words[col][i:i+M] == words[col][i:i+M][::-1]:
            	ret=words[row][i:i+M]
    
    print('#{} {}'.format(test_case, ret))
    # ///////////////////////////////////////////////////////////////////////////////////
