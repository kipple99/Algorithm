# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
    return my_list

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    b = 0
    p = end
    for i in range(end): # 범위를 pivot 앞까지 봐야해서 range(end)로 구현
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
    
    swap_elements(my_list, p, b)
    p = b
    
    return p

# 퀵 정렬 (start, end 파라미터 없이도 호출이 가능하도록 수정해보세요!)
def quicksort(my_list, start=0, end=None):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    if end == None:
        end = len(my_list) - 1
    
    # base case
    # quicksort 함수는 재귀적으로 호출되며, 파라미터 start와 end만 바뀔뿐, my_list는 변하지 않는다.
    if end - start < 1: # end - start == 0 (x)
        return # return None과 같은 효과
    
    p = partition(my_list, start, end)
    
    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, p-1)
    
    
    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, p+1, end)

# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)
