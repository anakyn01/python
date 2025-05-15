#개발자는 개발자가 정하는 조건이 발생할때 사용자정의오류를 만듭니다
x = 3

if not type(x) is int: #만약 변수 x에 타입이 숫자가 아니라면
    raise TypeError("숫자가 아닌 문자열을 적으셨어요")

try:
    print("세계여 안녕" + "hello world")
except:
    print("무언지 모르 겠지만 잘못되었음")
else:
    print("난 오류가 안났을때만 실행됨")

try:
    f = open("demofile.txt")
    try:
        f.write("메모장에 글을 써 보아요")
    except:
        print("글을 쓸수가 없습니다")
    finally:
        f.close()
except:
    print("파일을 여는 중 오류가 발생했습니다")
    



test = '''
1) try => 코드블럭에 오류가 있는지 없는지를 테스트한다
2) except => 사용하면 오류를 처리할수 있습니다
3) else => 오류가 없을때 코드를 실행할수 있습니다
4) finally => 코브블록에 결과와 상관없이 코드를 실행
'''