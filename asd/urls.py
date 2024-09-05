from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('2222/', views.page_2222_view, name='page_2222'),  # 메인메뉴 목록(이름정해야됨)
    path('3333/', views.page_3333_view, name='page_3333'),  # 메인메뉴 목록(이름정해야됨) 
    path('4444/', views.page_4444_view, name='page_4444'),  # 메인메뉴 목록(이름정해야됨)
    path('5555/', views.page_5555_view, name='page_5555'),  # 메인메뉴 목록(이름정해야됨)
    path('service1/', views.service1_view, name='service1'),  # 자주 이용하는 서비스1(이름 정하기)
    path('service2/', views.service2_view, name='service2'),  # 자주 이용하는 서비스2(이름 정하기)
    path('service3/', views.service3_view, name='service3'),  # 자주 이용하는 서비스3(이름 정하기)
    path('login/', views.login_view, name='login'),  # 로그인
    path('signup/', views.signup_view, name='signup'),  # 회원가입
    path('mypage/', views.mypage_view, name='mypage'),  # 마이페이지
    path('quick_menu2/', views.quick_menu2, name='quick_menu2'),  # 오른쪽 메뉴 2(이름 정하기)
    path('quick_menu3/', views.quick_menu3, name='quick_menu3'),  # 오른쪽 메뉴 3(이름 정하기)
    path('quick_menu4/', views.quick_menu4, name='quick_menu4'),  # 오른쪽 메뉴 4(이름 정하기)
    path('quick_menu5/', views.quick_menu5, name='quick_menu5'),  # 오른쪽 메뉴 5(이름 정하기)

]
