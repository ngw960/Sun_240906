from django import forms
from .models import User

class LoginForm(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    # 비밀번호 확인 기능
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

