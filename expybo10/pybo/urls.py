from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo' # 별칭 지정

# 해당 모듈명이 표시되도록 변경(views.index -> base_views.index)
urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'), # 질문 수정
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'), # 질문 삭제

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'), # 답변 수정
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'), # 답변 삭제

    # 제너릭 뷰 사용시
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.DetailView.as_view()),
]

# 장고는 디버깅시 보통 urls.py 파일에서 URL에 매핑된 함수를 찾는것으로 시작
# 다음과 같은 방식 사용시 urls.py 파일에 매핑된 함수명은 알수 있지만 어떤 뷰 파일의 함수인지는 알 수가 없음
# views 디렉터리의 모든 뷰 파일을 찾아봐야 됨
# 위의 방식인 해당 모듈명이 표시되도록 변경
'''
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'), # 질문 수정
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'), # 질문 삭제
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'), # 답변 수정
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'), # 답변 삭제
'''
