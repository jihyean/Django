from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST": # POST 요청일시 화면에서 입력한 데이터로 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1') # 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수
            
            # 신규 사용자를 생성한 후에 자동 로그인
            # authenticate와 login함수는 django.contrib.auth 모듈의 함수로 사용자 인증과 로그인을 담당
            user = authenticate(username=username, password=raw_password)  # 사용자 인증(사용자명과 비밀번호가 정확한지 검증한다)
            login(request, user)  # 로그인(사용자 세션을 생성한다)

            return redirect('index')
    else: # GET 요청일시 회원가입 화면
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
