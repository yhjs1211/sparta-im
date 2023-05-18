from flask import Flask

# Flask 인스턴스 생성
app = Flask(__name__)

# 웹 표현 : route() 메소드 사용

@app.route('/')

# @가 붙는 것은 장식자(decorator)를 나타냄.
# flask에서 이러한 장식자가 URL 연결에 활용
# 장식자를 사용하면 다음 행의 함수부터 장식자가 적용된다.

def hello():
    return 'Hello world'



if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)