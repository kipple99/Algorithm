# 방법 1

def sublist_max(profits):
    # 여기에 코드를 작성하세요
    sub_list = []
    for i in range(len(profits)):
        sub_list.append(sum(profits[:i+1]))
        
    return max(sub_list)

################################################

# 방법 2

def sublist_max(profits):
    # 여기에 코드를 작성하세요
    sub_list = []
    sum = 0
    for i in range(len(profits)):
        for j in range(i+1):
            sum += profits[j]
        sub_list.append(sum)
        sum = 0
        
    return max(sub_list)
    
################################################

# 방법 3

def sublist_max(profits):
    max_profit = profits[0] # 최대 수익
    
    for i in range(len(profits)):
        # 인덱스 i부터 j까지 수익의 합을 보관하는 변수
        total = 0
        
        for j in range(i, len(profits)):
            # i부터 j까지 수익의 합을 계산
            total += profits[j]
            
            # i부터 j까지 수익의 합이 최대 수익이라면, max_profit 업데이트
            max_profit = max(max_profit, total)

    return max_profit


# 테스트 코드
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
