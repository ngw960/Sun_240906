from django import forms
from .models import SignUp_User, Panel

#------------------------------------------------------------------

# 폼 - 로그인
class LoginForm(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

#------------------------------------------------------------------
# 폼 - 회원가입
class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    # 회원가입 폼 모델 설정
    class Meta:
        model = SignUp_User  # 모델 이름 변경
        # 사용할 목록
        fields = ['username', 'email', 'password'] 
        # 적용할 위젯
        widgets = {
            'password': forms.PasswordInput(),
        }

    # 재확인 - 비밀번호
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")\
#------------------------------------------------------------------
# 폼 - 패널
# class PanelForm(forms.ModelForm):
#     class Meta:
#         model = Panel
#         fields = ['username', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

    