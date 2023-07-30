def sum_in_list(search_sum, sorted_list):
    # 여기에 코드를 작성하세요
    sum = 0
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            sum = sorted_list[i] + sorted_list[j]
            if search_sum == sum:
                return True
            else:
                continue
    
    return False

######################################################

def sum_in_list(search_sum, sorted_list):
    # 여기에 코드를 작성하세요
    low = 0
    high = len(sorted_list) - 1
    while low < high:
        if search_sum > (sorted_list[low] + sorted_list[high]):
            low += 1
        elif(search_sum < (sorted_list[low] + sorted_list[high])):
            high -= 1
        else:
            return True
    return False
            


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))