from django.db import models

# 사용자 모델 규칙 - 이름, 비밀번호, 이메일 (중복불가능 및 길이 제한)
class SignUp_User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    
    # 사용자 이름 문자열로 변환
    def __str__(self):
        return self.username
    
class Panel(models.Model):
    capacity = models.FloatField(verbose_name="설치 용량")
    location = models.CharField(max_length=255, verbose_name="설치 지역")
    modelNamev = models.CharField(max_length=255, verbose_name="모델명", null=True, blank=True)
    manufacturer = models.CharField(max_length=255, verbose_name="제조업체", null=True, blank=True)
    maintenance = models.CharField(max_length=255, verbose_name="관리업체", null=True, blank=True)
    quantity = models.IntegerField(verbose_name="보유 개수")
    size = models.FloatField(verbose_name="크기 (m²)", null=True, blank=True)
    date = models.DateField(verbose_name="설치일자", null=True, blank=True)
    record = models.DateField(verbose_name="점검기록 (yyyy-mm-dd)", null=True, blank=True)
    cause = models.CharField(max_length=255, verbose_name="고장원인", null=True, blank=True)