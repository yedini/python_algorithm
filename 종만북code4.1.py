## 주어진 배열에서 가장 많이 등장하는 숫자를 반환하기

# 주어진 배열 A에서 가장 많이 등장하는 숫자를 반환한다.
# 만약 두 가지 이상 있을 경우 아무 것이나 반환한다.

def majority1(numbers):
    majority_count=0
    for num in numbers:
        count=0
        for i in range(len(numbers)):
            if numbers[i] == num:
                count += 1
        if count > majority_count:
            majority=num
            majority_count=count
    return majority

print(majority1([22,35,1,7,22,30,35]))
