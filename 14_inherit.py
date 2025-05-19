class Person :
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def talking(self):
        print(self.firstname, self.lastname)

class Child(Person):
    pass

q = Child("윤희","이")
q.talking()








class Pr:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
#1) 클래스 패런츠가 생성자로 성과 이름에 틀을 만듬
    def printname(self):
        print(self.firstname, self.lastname)

anyOne = Pr("영일","황")
anyOne.printname()

inH = '''
Python Inheritance 상속
- 부모클래스는 상속시키는 클래스로 기본 클래스 라고 합니다
- 자식클래스는 부모클래스로 부터 상속받는 클래스로 파생 클래스라고도 합니다
'''
print(inH)