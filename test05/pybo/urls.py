from django.urls import path

from . import views

app_name = 'pybo' # 별칭 지정

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

    # 제너릭 뷰 사용시
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.DetailView.as_view()),
]
