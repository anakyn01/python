i = 0 #1부터 시작
while i <= 6:#i가 6보다 작을때 까지 i는 개별증가
    print(i)
    i += 1 #지정된 범위까지 1씩 증가하세요

#break : 조건이 참이더라도 루프를 중지합니다
q = 0
while q < 7:
    print(q)
    if (q == 3):#만약 개별중에 3과 같다면 루프중지
        break
    q += 1

#continu : 지정한 엘리먼트를 건너뛰고 다음 엘리먼트로 넘어갑니다
print("=====================================")
w = 0
while w < 5:
    w += 1
    if w == 2:
        continue
    print(w)
    
#else : else문을 사용하면 조건이 더이상 참이 아닐때 코드블록을 한번더 실행할수 있습니다
i = 3
while i < 7:
    print(i)
    i += 1
else:
    print("seven")
'''
파이선루프 (javascript, react,vue, java ...)
- 파이선에는 두개의 기본 루프명령이 있습니다
for 루프
while 루프
루프를 실행하면 조건인 참인 동안 일련의 명령문을 수행할수 있다
'''