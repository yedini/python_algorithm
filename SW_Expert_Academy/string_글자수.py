T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    str1=input()
    str2=input()
    c=0  #count
    mc=0  #count한 값들중 최대값
    for i in str1:
        for j in str2:
            if i == j:
                c += 1
        if mc < c:
            mc=c
        c=0
    print('#{} {}'.format(test_case, mc))