from django.db import models

# 사용자 모델 규칙 - 이름, 비밀번호, 이메일 (중복불가능 및 길이 제한)
class SignUp_User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    
    # 사용자 이름 문자열로 변환
    def __str__(self):
        return self.username