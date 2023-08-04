def find_same_number(some_list, start = 1, end = None):
    # 필요한 경우, start와 end를 옵셔널 파라미터로 만들어도 됩니다.
    # 여기에 코드를 작성하세요
    
    if end == None:
        end = len(some_list)
        
    # 반복된 요소를 찾으면 리턴
    if start == end:
        return start
    
    # 중간 지점을 구한다.
    mid = (start + end) // 2
    
    # 왼쪽 범위의 숫자를 센다. 오른쪽은 리스트길이에서 왼쪽 길이를 빼면 되기 때문에 세지 않는다
    left_count = 0
    
    for element in some_list:
        if start <= element and element <= mid:
            left_count += 1
            
    # 왼쪽과 오른쪽 범위중 과반 수 이상의 숫자가 있는 범위 내에서 탐색을 다시한다
    # mid - start + 1 인 이유 : 보통 1부터 10까지 개수를 셀 때 10 - 1 + 1과 같이 센다.
    # 즉 갯수를 세어나갈때는 범위의 끝값 - 처음값 + 1을 해야 1부터 10까지의 개수가 나타난다.
    # 왼쪽 갯수가 왼쪽 범위의 갯수보다 많다면 중복되는 값을 찾기 위해 다시 왼쪽으로 재귀
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)
    
    # 오른쪽 범위안에서 중복되는 항목을 찾기 위해 다시 오른쪽 범위로 다시 재귀
    return find_same_number(some_list, mid + 1, end)

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))