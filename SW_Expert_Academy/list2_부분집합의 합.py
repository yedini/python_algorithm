# 부분집합 모두 구하기
nums=[i for i in range(1,13)]
subs=[]
for i in range(1 << 12):
    temp=[]
    for j in range(12):
        if i & (1 << j):
            temp.append(nums[j])
    subs.append(temp)

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K=map(int, input().split())
    
    #원소 개수가 N개인 부분집합 구하기
    len_list = []
    for i in subs:
        if len(i)==N:
            len_list.append(i)
    
    #합이 K인 부분집합의 개수 구하기
    ret = 0
    for i in len_list:
        if sum(i) == K:
            ret += 1
    print("# {} {}".format(test_case, ret))