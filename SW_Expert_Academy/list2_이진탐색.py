T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    P,A,B=map(int, input().split())
    
    #A의 시행횟수
    left=1
    right=P
    Atry=0
    Btry=0
    while 1:
        C=int((left+right)/2)
        Atry += 1
        if C == A:
            break
        elif C < A:
            left=C
        else: 
            right=C
            
    #B의 시행횟수
    left=1
    right=P
    while 1:
        C=int((left+right)/2)
        Btry += 1
        if C == B:
            break
        elif C < B:
            left=C
        else: 
            right=C
    if Atry > Btry: ret='B'
    elif Btry > Atry: ret='A'
    else: ret='0'
    print('# %d %c' %(test_case, ret))