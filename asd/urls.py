from django.urls import path
from . import views

urlpatterns = [
    # 메인메뉴
    path('', views.main_view, name='home'),
    path('1111/', views.page_1111_view, name='page_1111'),  # 메인메뉴 목록(이름정해야됨)
    path('2222/', views.page_2222_view, name='page_2222'),  # 메인메뉴 목록(이름정해야됨)
    path('3333/', views.page_3333_view, name='page_3333'),  # 메인메뉴 목록(이름정해야됨) 
    path('4444/', views.page_4444_view, name='page_4444'),  # 메인메뉴 목록(이름정해야됨)
    path('5555/', views.page_5555_view, name='page_5555'),  # 메인메뉴 목록(이름정해야됨)

    # 자주 이용하는 서비스
    path('service1/', views.service1_view, name='service1'),  # 자주 이용하는 서비스1(이름 정하기)
    path('service2/', views.service2_view, name='service2'),  # 자주 이용하는 서비스2(이름 정하기)
    path('service3/', views.service3_view, name='service3'),  # 자주 이용하는 서비스3(이름 정하기)
    path('login/', views.login_view, name='login'),  # 로그인
    path('signup/', views.signup_view, name='signup'),  # 회원가입

    # 퀵메뉴(오른쪽 메뉴)
    path('mypage/', views.mypage_view, name='mypage'),  # 마이페이지
    path('panel_info/', views.panel_info_view, name='panel_info'),  # 패널 정보
    path('Last_accessed/', views.Last_accessed_view, name='Last_accessed'),  # 최근 접속
    path('contact_us/', views.contact_us_view, name='contact_us'),  # 문의 방법

    # 하단 메뉴
    path('privacy/', views.privacy_view, name='privacy'),  # 개인정보 처리 방침
    path('terms/', views.terms_view, name='terms'),  # 이용약관
    path('sitemap/', views.sitemap_view, name='sitemap'),  # 사이트맵
    path('address/', views.address_view, name='address'),  # 주소
   
   # 로그인 페이지
    path('find_id_pw/', views.find_id_pw_view, name='find_id_pw'),  # 아이디/비밀번호 찾기 페이지


]
