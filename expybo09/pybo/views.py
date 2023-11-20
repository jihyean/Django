from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator # 페이지네이션 
from django.contrib.auth.decorators import login_required # 로그인 / 로그아웃 상태 처리
from django.contrib import messages



def index(request):
    page = request.GET.get('page', '1')  # 페이지 ex) http://localhost:8000/pybo/?page=1
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

# 로그아웃 상태에서 해당 함수 호출시
# User 객체가 아닌 AnonymousUser 객체가 들어옴
# 해당 어노테이션을 활용하여 로그인된 상태에서만 가능토록 함
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

    
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

# 답변 수정
@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


# 답변 삭제
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)



''' 제너릭 뷰 사용시
class IndexView(generic.ListView):
    def get_queryset(self):
        return Question.objects.order_by('-create_date')


class DetailView(generic.DetailView):
    model = Question
'''
