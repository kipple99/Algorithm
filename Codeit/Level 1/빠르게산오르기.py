def select_stops(water_stops, capacity):
    # 여기에 코드를 작성하세요
    answer = []

    # 마지막으로 들른 약수터 위치
    last_stop = 0
    
    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1의 지점 약수터를 들른다.
        # (water_stops[i] - last_stop <= capacity 이런식으로 비교해버리면, 해당 코드가 모호해짐. 갈 수 없는 위치를 찾고 바로 전 위치가 최댓 값이라는 설정)
        if water_stops[i] - last_stop > capacity:
            answer.append(water_stops[i - 1])
            last_stop = water_stops[i - 1]
            
    # 마지막 약수터는 무조건 간다
    answer.append(water_stops[-1])
        
    return answer
            
         
# 테스트 코드
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))