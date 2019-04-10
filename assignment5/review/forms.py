from django import forms
from .models import WritingContents

class ContentsForm(forms.ModelForm):
    class Meta:
        model = WritingContents
        fields = ('title', 'contents', 'price', 'score',)
#포스트의 제목 밖에 안보일 때, 제목 외의 어떤 정보를 볼 것인지 설정할 수 있는 클래스다.