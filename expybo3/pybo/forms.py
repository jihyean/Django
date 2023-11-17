from django import forms
from pybo.models import Question, Answer

# 질문 폼
class QuestionForm(forms.ModelForm):
    #모델 폼(forms.ModelForm)을 상속
    # 모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할수 있는 폼

    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성

        '''
        # 폼 위젯
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        '''

        # 폼 레이블
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

# 답변 폼
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }