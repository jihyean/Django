from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common' # 별칭 지정

urlpatterns = [
    # LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾음
    # 로그인은 common 앱에서 구현할 것으므로 참조 위치를 변경
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #{% url 'common:logout' %}에 대응하는 URL 매핑
]
