from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    #  User 모델은 django.contrib.auth 앱이 제공하는 사용자 모델로 회원 가입시 데이터 저장에 사용했던 모델
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #  계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일시

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일시
