# date : 20240129
# desc : 연산자

## 사칙연산 - 더하기, 빼기, 곱하기, 나누기(3가지 = 나누기, 정수로 나누기, 나눈 나머지)
## =(값을 할당), ==(비교), > < >= <= !=(같지 않다) **(제승) -> 비교연산
## and, or, not 논리 연산

print(2*10)
print(2**10)

print(5 / 2) # 2.5 실수로 나누기
print(5 // 2) # 2 정수로 나누기
print(5 % 2) # 정수로 나누고, 남은 나머지
print(5 == 4) #False
print(5 >= 4) #true
print(5 > 4) 
print(5 < 4)
print(5 != 4)

print(5 <= 4 and (5/2 < 3)) # False and 기준으로 왼쪽 오른쪽 모두 참이여야 참
print(5 > 4 or (5/2 < 3)) # True or 기준으로 왼쪽 or 오른쪽 둘 중 하나 참 이여야 함
print(not (5 > 4)) # 참이면 거짓, 거짓이면 참 반대로