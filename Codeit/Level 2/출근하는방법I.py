# 시간 복잡도 O(n)
def staircase(n):
    # 여기에 코드를 작성하세요
    a, b = 1, 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
        
    return a

# 테스트 코드
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))