T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m=map(int, input().split(' '))
    nums=list(map(int, input().split(' ')))
    adds=[]
    for i in range(n-m+1):
        adds.append(nums[i]+nums[i+1]+nums[i+2])
    ret=max(adds)-min(adds)
    print('#',str(test_case),str(ret))