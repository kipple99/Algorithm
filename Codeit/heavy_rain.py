def trapping_rain(buildings):
    # 여기에 코드를 작성하세요
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0
    
    # 첫번째와 마지막 인덱스는 볼 필요가 없다.
    for i in range(1, len(buildings)-1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])
        
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)
        
        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])
    
    return total_height
        
            
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
