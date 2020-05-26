#### 주어진 칸에서 시작해서 특정 단어를 찾을 수 있는지 확인하는 함수
# 보글 게임판의 (x,y)에서 시작하는 단어의 존재를 파악한다.


##기저 사례
# 1. 위치(x,y)에 있는 글자가 원하는 단어의 첫 글자가 아닌 경우 항상 실패
# 2. 1번에 해당하지 않을 경우, 원하는 단어가 한 글자인 경우 항상 성공

#boggle 게임판 형성 : 5행 5열의 리스트
boggle=[['u','r','l','p','m'],['x','p','r','e','t'],['g','i','a','e','t'],
['x','t','n','z','y'],['x','o','q','r','s']]

# x: 시작하는 행의 위치
# y: 시작하는 열의 위치
# word: 찾고자 하는 단어

side=[[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1],[0,-1],[0,1]]
def hasWord(x,y, word):
    #기저 사례
    if x >4 or y >4 or x<0 or y<0 :    # |로 하면 안되고 or로 하자..! 잊지 말자
        return False
    if word[0] != boggle[x][y]:
        return False
    if len(word) == 1:
        return True

    #word의 첫번째 알파벳은 빼고 검사
    word=word[1:]

    #인접한 여덟 칸을 검사
    for s in side:
        if hasWord(x+s[0], y+s[1], word):
            return True
    
    return False


print(hasWord(1,1,'pretty'))
