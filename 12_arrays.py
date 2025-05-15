cars = ["merecedes", "bmw", "ford"]
print(cars)
#배열에 요소추가 append() : 오른쪽에 추가
cars.append("현대")
print(cars)
#배열에서 요소제거 pop() 과 인덱스번호 사용
cars.pop(1)
print(cars)

#배열의 요소에 접근하기 인덱스 번호로 참조합니다 0,1,2
x = cars[0]
y = cars[1]
z = cars[2]
print(x,y,z)
#배열의 길이 (size가 아닌 갯수) lengh => len
q = len(cars)
print(q)

'''
배열의 매서드
append() : 새로추가
clear() : 모든요소를 제거
copy() : 복사
count() : 지정된 값을 갖는 갯수를 리턴 
extend() : 리스트에 리스트를 추가 
index() : 예를 들어 one two one에서 첫번째 인덱싱을 지정
insert() : 인덱스를 지정하여 삽입합니다 
cars.insert(3, "sm")
pop() : 지정한 인덱스 요소를 제거
remove() : 동일한 값이 여러게 있을때 그 첫번째 엘리먼트만 제거
reverse() : 순서를 반대로 바꿉니다
sort() : [s,w,g,h,a] 정렬
'''


#가로가 아닌 지정된 범위만큼 블록으로 출력할때
for m in cars:#forEach 객체를 출력할때
    print(m)
'''
단일변수에 여러값을 담을때 사용한다
일반적으로 자바스크립트에는 array가 존재한다
그러나 파이선은 array가 없다
그래서 리스트로 대체한다
만약 파이선에서 어레이를 사용하려면 Numpy를 설치해야됨
'''