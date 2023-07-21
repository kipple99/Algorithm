def fib_memo(n, cache):
    # 여기에 코드를 작성하세요
    # base case
    if n < 3: # 피보나치 수열의 첫 번째 수와 두번째 수는 1로 정해져있다.
        return 1
    
    # recursive case
    if n in cache: # 이미 n번째 피보나치를 계산했으면
        return cache[n] # 저장된 값 바로 리턴
    
    # 아직 n번째 피보나치 수를 계산하지 않았다면
    # 계산한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    
    # 계산한 값 return
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))
