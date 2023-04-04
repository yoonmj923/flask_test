'''
    - GET방식으로 데이터 전송하기
        - 클라이언트 (키=값&키=값...)
            - 링크 => 화면 전환
                <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
            - form 전송, 화면 껌벅 => 화면 전환
                <form action="http://127.0.0.1:5000/link" method="get">
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송"/>
                </form>
            - ajax 가능 (jQuery로 표현), 화면은 현재 화면유지
                $.get({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:( res )=>{},
                    error:(err)=>{}
                })
        - 서버
            - get 방식 데이터 추출
            - name = request.args.get('name')
            - age  = request.args.get('age')

    - /link쪽으로 요청하는 방식은 다양할수 있다. 단 사이트 설계상 1가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링 할것인가? 보안의 기본사항
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/link')
def link():
    # request.args['age'] => 데이터 누락시 서버 셧다운됨, 사용 하면 않됨
    # request.args.get('age') => 데이터 누락시 None이 나와서 예외처리 가능함
    name = request.args.get('name')
    age  = request.args.get('age')
    return "[%s] [%s]" % (name, age)

@app.route('/test')
def test():
    # 엔트리포인트(진입로, 프로그램 시작점)과 같은 경로에 templates/test.html 생성
    return render_template('test.html')

if __name__ == "__main__":    
    app.run(debug=True)