'''파이선 수학'''
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x, y)

#abs()함수는 지정된 숫자의 절대값(양수를 의미)
x = abs(-7.325)
print(x)

#g-dragon power pow 4, 3 4 * 4 * 4
e = pow(4, 3)
print(e)

#수학함수를 사용할때는 import math를 해야합니다
import math
x = math.sqrt(64)
print(x) #8

#올림(무조건 올림)과 내림(무조건 내림)
x = math.ceil(1.4) #2
y = math.floor(1.4) #1
print(x)
print(y)

t = math.pi
print(t)