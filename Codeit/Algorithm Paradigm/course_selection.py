def course_selection(course_list):
    # 여기에 코드를 작성하세요
    early_time = []
    sorted_list = sorted(course_list, key=lambda x: x[1]) # lambda x: 뒤에 인덱스 0, 1 조정
    early_time.append(sorted_list[0])
    
    for i in sorted_list: 
        if i[0] > early_time[-1][1]:
            early_time.append(i)

    return early_time
        
        
    


# 테스트 코드
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
