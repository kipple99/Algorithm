def max_product(left_cards, right_cards):
    # 여기에 코드를 작성하세요
    max_num = []
    
    for i in left_cards:
        for j in right_cards:
            max_num.append(i * j)
    
    return max(max_num)
    
# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
