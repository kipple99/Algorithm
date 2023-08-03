# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 여기에 코드를 작성하세요
    # 계단 높이가 0이거나 1이면 올라가는 방법은 한가지 밖에 없다.
    number_of_ways = [1, 1]
    
    # 이 변수들을 업데이트해 주며 n번째 계단을 오르는 방법의 수를 구한다.
    for height in range(2, stairs + 1):
        number_of_ways.append(0)
        
        for step in possible_steps:
            # 음수 계단 수는 존재하지 않기 때문에 무시한다.
            if height - step >= 0:
                number_of_ways[height] += number_of_ways[height - step]
                
    return number_of_ways[stairs]


##################################################################

def staircase(stairs, possible_steps):
    # 여기에 코드를 작성하세요
    if stairs < 0:
        return 0
    if stairs <= 1:
        return 1
    
    result = 0
    
    for i in possible_steps:
        result += staircase(stairs - i, possible_steps)
    
    return result
        

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))