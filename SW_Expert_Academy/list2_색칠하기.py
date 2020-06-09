T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    squarenum=int(input())  # 색칠영역 개수
    col=[set(), set()]   #col[0]은 빨강, col[1]은 파랑
    for i in range(squarenum):
        x1, y1, x2, y2, color=map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                col[color-1].add((x,y))
    ret=len(col[0] & col[1])
    print('# {} {}'.format(test_case, ret))                             