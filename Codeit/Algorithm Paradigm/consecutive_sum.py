def consecutive_sum(start, end):
    # 여기에 코드를 작성하세요
    # base case
    if start == end:
        return start
    
    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의한다.(Divide)
    mid = (start + end) // 2
    
    # 각 부분을 재귀적으로 풀고(conquer), 부분문제의 답을 서로 더한다.
    return consecutive_sum(start, mid) + consecutive_sum(mid+1, end)
        
    
    

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
