from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 로그인 성공 시 리다이렉트할 페이지
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def main_view(request):
    form = LoginForm()  # 빈 로그인 폼을 전달
    return render(request, 'main.html', {'form': form})

def page_2222_view(request):
    return render(request, '2222.html')  # 메인메뉴 목록(함수 이름정해야됨)

def page_3333_view(request):
    return render(request, '3333.html')  # 메인메뉴 목록(함수 이름정해야됨)

def page_4444_view(request):
    return render(request, '4444.html')  # 메인메뉴 목록(함수 이름정해야됨)

def page_5555_view(request):
    return render(request, '5555.html')  # 메인메뉴 목록(함수 이름정해야됨)

def service1_view(request):
    return render(request, 'service1.html')  # 자주 이용하는 서비스1(이름 정하기)

def service2_view(request):
    return render(request, 'service2.html')  # 자주 이용하는 서비스2(이름 정하기)

def service3_view(request):
    return render(request, 'service3.html') # 자주 이용하는 서비스3(이름 정하기)

def login_view(request):
    form = LoginForm()  # 빈 로그인 폼을 전달
    return render(request, 'login.html', {'form': form})

def signup_view(request):  # 회원가입 페이지                
    return render(request, 'signup.html')

def mypage_view(request):  # 마이페이지           
    return render(request, 'mypage.html')

def quick_menu2(request):  # 오른쪽 메뉴2 (이름 정하기)          
    return render(request, 'quick_menu2.html')

def quick_menu3(request):  # 오른쪽 메뉴3 (이름 정하기)          
    return render(request, 'quick_menu3.html')

def quick_menu4(request):  # 오른쪽 메뉴4 (이름 정하기)          
    return render(request, 'quick_menu4.html')

def quick_menu5(request):  # 오른쪽 메뉴5 (이름 정하기)         
    return render(request, 'quick_menu5.html')




