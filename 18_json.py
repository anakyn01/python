import json

#데이터 적인 요소들 즉 API
some = '{"name":"영일", "age":48, "city":"seoul"}'
#some은 json데이터이다 json인데 java개발하면 java로
#파이선이면 파이선으로 얘를 바꿔줘야합니다 형식에 맞게 바꾸는걸
#파싱한다

parseStr = json.loads(some)

print(parseStr["age"])

#파이선을 json으로 보내야 할때
x = {
    "name":"John", "age":30, "city":"New York"
}
y = json.dumps(x) #파이선 사전을 json으로 변환
print(y)

jsonWhat = '''
Java Script Object Notation
- 가벼운 데이터 교환형식
- 언어에 독립적
- 자체 설명적으로 이해하기 쉽다
- 데이터를 읽고 생성하는 코드는 어떤것도 json사용이 가능
java, php, react, vue 등 웬만한 개발에서 다 사용합니다
- 자바스크립트에서는 그냥 사용하지만 
파이선에서는 import로 불러옵니다
'''