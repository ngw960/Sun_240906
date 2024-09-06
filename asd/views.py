from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import SignUpForm
from .forms import LoginForm

#---------------------------------------------------------------

## 메인페이지
def main_view(request):
    form = LoginForm()
    return render(request, 'main.html', {'form': form})

## 메인페이지 - 상단 (목록)
def main_list_1_view(request):
    return render(request, 'main_list_1.html')  # 메인 목록1
def main_list_2_view(request):
    return render(request, 'main_list_2.html')  # 메인 목록2
def main_list_3_view(request):
    return render(request, 'main_list_3.html')  # 메인 목록3
def main_list_4_view(request):
    return render(request, 'main_list_4.html')  # 메인 목록4
def main_list_5_view(request):
    return render(request, 'main_list_5.html')  # 메인 목록5


## 즐겨찾기
def bookmark_1_view(request):
    return render(request, 'bookmark_1.html')  # 즐겨찾기 1
def bookmark_2_view(request):
    return render(request, 'bookmark_2.html')  # 즐겨찾기 2
def bookmark_3_view(request):
    return render(request, 'bookmark_3.html') # 즐겨찾기 3


## 바로가기
def quick_mypage_view(request):  # 마이페이지           
    return render(request, 'mypage_mypage.html')
def quick_panel_view(request):  # 패널정보
    return render(request, 'mypage_panel.html')
def quick_recent_view(request):  # 최근접속 
    return render(request, 'main_recent.html')
def quick_contact_view(request):  # 문의방법
    return render(request, 'main_contact.html')


## 메인페이지 - 하단 (정보)
def down_privacy_view(request):  # 개인정보 처리방침        
    return render(request, 'down_privacy.html')
def down_terms_view(request):  # 이용약관         
    return render(request, 'down_terms.html')
def down_sitemap_view(request):  # 사이트맵        
    return render(request, 'down_sitemap.html')

#---------------------------------------------------------------

## 회원가입
# 회원가입 창
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'asd/user/basic/signup.html', {'form': form})

# 중복확인_아이디
def signup_duplicate_id(request):
    username = request.GET.get('username', None)
    if username and User.objects.filter(username=username).exists():
        return JsonResponse({'exists': True})
    return JsonResponse({'exists': False})

# 중복확인_이메일
def signup_duplicate_email(request):
    useremail = request.GET.get('email', None)
    if useremail and User.objects.filter(email=useremail).exists():
        return JsonResponse({'exists': True})
    return JsonResponse({'exists': False})
#---------------------------------------------------------------

## 로그인
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


## 회원정보 찾기
def find_id_view(request):  # 아이디 찾기      
    return render(request, 'find_id.html')
def find_pw_view(request):  # 비밀번호 찾기      
    return render(request, 'find_pw.html')

## 마이페이지
# 마이페이지 홈
# 회원정보 조회
# 회원정보 수정 - 본인확인(비밀번호 입력)
# 회원정보 수정 - 수정 페이지

#---------------------------------------------------------------

