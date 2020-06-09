T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import Counter
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=input()
    nums=[int(x) for x in input()]
    counts=[x for x in Counter(nums).values()]
    for i in range(len(nums)):

        
        if counts[i] == max(counts):
            what=nums[i]
            howmany=counts[i]
    print('#{} {} {}'.format(test_case, what, howmany))
