T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    numbers=sorted(list(map(int, input().split())))
    new_list=[]
    for i in range(n):
        if i % 2 == 1:
            t=numbers.pop(0)
            new_list.append(t)
        else:
            t=numbers.pop()
            new_list.append(t)
        ret=''
        for i in new_list[:10]:
            ret=ret+' '+str(i)
    print('#{}{}'.format(test_case, ret))