## 참고: https://gurumee92.tistory.com/153

def quad(strings, index):
    if index >= len(strings):
        return ""
    if strings[index] =='w':
        return 'w'
    if strings[index] == 'b':
        return 'b'
    
    index += 1
    lt = quad(strings, index)
    
    index += len(lt)
    rt = quad(strings, index)

    index += len(rt)
    lb = quad(strings, index)

    index += len(lb)
    rb = quad(strings, index)

    return 'x' + lb + rb + lt + rt


print(quad('xbwwb', 0))
print(quad('xbwxwbbxb', 0))