def power(x, y):
    # 여기에 코드를 작성하세요
    # Base case
    if y == 0:
        return 1
    
    # 계산을 한 번만 하기 위해 변수에 저장
    subresult = power(x, y // 2)
    
    # Recursive Case
    # 문제를 문제 두 개로 나눠준다.(짝수인 경우, 홀수인 경우)
    # y가 한번은 홀수가 된다.
    if y % 2 == 0:
        return subresult * subresult
    else:
        return x * subresult * subresult


# 테스트 코드
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))