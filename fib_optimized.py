def fib_optimized(n):
    # 여기에 코드를 작성하세요
    curent = 1
    previous = 0
    
    if n > 1:
        for i in range(1, n):
            temp = curent
            curent = curent + previous
            previous = temp
            # curent, previous = curent + previous, curent
            
        return curent
    
    return curent


# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

