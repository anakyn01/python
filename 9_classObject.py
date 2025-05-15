class MyClass:
    x = 5 #프로퍼티

p1 = MyClass() #객체
#임의에 변수 p1은 부모인 MyClass를 상속받음
print(p1.x)

#유산을 물려주지 않고 스킬을 물려줌
class Person:
    def __init__(self, name, age):#파이선에 함수
        self.name = name
        self.age = age
        
hyi = Person("young-il", 47) #객체
print("내 이름은 ", hyi.name," 이며 나이는 ",  hyi.age, " 입니다")



what = '''
파이선은 객체지향 프로그래밍 언어입니다
- 파이선의 거의 모든것은 속성과 메서드를 갖춘 객체입니다
- 클래스는 객체 생성자나 객체를 만드는 청사진과 같습니다
'''
print(what)