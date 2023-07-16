def fib_tab(n):
    # 여기에 코드를 작성하세요
    # tabulation
    fib_table = [0, 1, 1]
    
    if n > 2:
        for i in range(3, n+1):
            fib_sum = fib_table[i-1] + fib_table[i-2]
            fib_table.append(fib_sum)
            # fib_table[i] = fib_table[i-1] + fib_table[i-2]
            # 빈 리스트는 index가 없기 때문에 위와 같이 할 수 없다. 
            
        return fib_table[n] 
    
    return fib_table[n]
            
        

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))