'''
    wtf를 활용하여 Form을 디자인함(FlaskForm을 상속받아서 재정의한다)    
'''
from flask_wtf import FlaskForm
# 데이터베이스상 테이블의 컬럼의 타입과 연관을 맺는다
# StringField : varchar(32) -> 글자수 제한이 있는 데이터를 받을때 지정
# TextAreaField :  text -> 글자수 제한이 없는 경우, (ex) 65535개 글자수)
from wtforms import StringField, TextAreaField 
# 유효성 검사용 옵션 가져오기
from wtforms.validators import DataRequired, Length, Email
# pip install email_validator 설치

class FormQuestion(FlaskForm):
    # 클레스 변수만 지정
    # 변수명 => id값, name값, '제목' => label 값이 됨
    title   = StringField('제목', validators=[ DataRequired('제목 입력 필수'), Email() ])
    content = TextAreaField('내용', validators=[ DataRequired() ])
    pass