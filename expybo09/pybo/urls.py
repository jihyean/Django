from django.urls import path

from . import views

app_name = 'pybo' # 별칭 지정

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'), # 질문 수정
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'), # 질문 삭제
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'), # 답변 수정
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'), # 답변 삭제
    

    # 제너릭 뷰 사용시
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.DetailView.as_view()),
]
