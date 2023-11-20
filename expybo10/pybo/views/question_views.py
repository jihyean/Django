from django.contrib import messages
from django.contrib.auth.decorators import login_required # 로그인 / 로그아웃 상태 처리
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

# question_create, question_modify, question_delete

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴받는다.
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

# 질문 수정
# messages는 장고가 제공하는 모듈로 넌필드 오류(non-field error)를 발생시킬 경우에 사용
# form 태그에 action 속성이 없는 경우 디폴트 action은 현재 페이지
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다') # 넌필드 오류(non-field error) 발생
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        #  instance를 기준으로 QuestionForm을 생성하지만 request.POST의 값으로 덮어쓰라는 의미
        # POST 요청인 경우 수정된 내용을 반영해야 하는 케이스이므로 다음처럼 폼을 생성
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장(현재일시)
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question) # GET 요청인 경우 질문수정 화면에 조회된 질문의 제목과 내용이 반영될 수 있도록 다음과 같이 폼을 생성
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

# 질문 삭제
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')