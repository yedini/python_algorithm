# 울타리에서 잘라낼 수 있는 직사각형의 최대 크기 구하기

def solve(left, right,h):

    #기저사례: 판자가 1개인 경우
    if left == right :
        return h[left]
    
    #[left,mid], [mid+1, right] 두 구간으로 문제를 분할한다.
    mid=(left+right)//2
    #[left, mid], [mid+1, right] 중 큰 직사각형 구하기
    ret=max(solve(left, mid,h), solve(mid+1, right,h))
    # 두 부분에 모두 걸치는 사각형 중 가장 큰 사각형 찾기: 가장 중간의 판자부터 시작
    lo = mid
    hi=mid+1
    height=min(h[lo], h[hi])
    ret= max(ret, height * 2)   #두개의 사각형 고려했으니까 너비가 2!

    #판자를 하나씩 넓혀가며 전체 사각형까지 확장한다
    #이 때 높이가 더 높은 쪽으로 확장함!
    while(left < lo or hi <right) :
        if hi < right and (lo == left or h[lo-1] < h[hi+1]) : #오른쪽이 더 큰 경우
            hi+=1
            height=min(height, h[hi])
        else:
            lo-=1
            height=min(height, h[lo])
        ret=max(ret, height*(hi-lo+1))
    return ret

tc1=[7,1,5,9,6,7,3]
tc2=[1,4,4,4,4,1,1]
tc3=[1,8,2,2]
print(solve(0,len(tc1)-1, tc1))
print(solve(0, len(tc2)-1, tc2))
print(solve(0, len(tc3)-1, tc3))