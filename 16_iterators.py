class MyNumbers:
    def __iter__(self):
        self.a = 1 #숫자1인데
        return self
    def __next__(self):
#반복을 중지하고 싶을때 가정법을 사용한다
     if self.a <= 20:
        x = self.a
        self.a += 1
        return x
     else:
         raise StopIteration
    #지정이 안되어 있어서

myChild = MyNumbers()
myiter = iter(myChild)

for x in myiter:
    print(x)

'''print(next(myiter))
print(next(myiter))
print(next(myiter))'''

#편리한 반복은 forEach 예를 들어 내가 검색하는데 지정한 만큼은 검색이 되어야 하기 떄문에
mystr = "banana"
for x in mystr:
    print(x)
    

mytuple = ("a" ,"b","c")
#개별반복
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

myStr = "banana" #반복 지정된 작업량 1-6 중복 똑같은 same
myit = iter(myStr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
'''
파이선 반복자
- 반복자는 셀수 있는 개수의 값을 담고 있는 객체입니다
- 팩키지 패키지 매터리얼 머티리얼
- 반복자는 반복이 가능한 객체로 모든 값을 탐색할수 있다는 의미입니다
- 매서드 __iter__() , __next__() 구현합니다
- 리스트, 튜플, 딕셔너리, 셋은 모두 반복 가능한 객체입니다

'''