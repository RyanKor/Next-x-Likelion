from django.db import models
from django.utils import timezone
# Create your models here.

class WritingContents(models.Model): #게시글 작성을 위해 DB에 입력되어야할 내용들을 추가시키는 Class
    title = models.CharField(max_length = 200, help_text = '최대 200자 입력가능') #제목 입력 기능
    contents = models.TextField() # book review에 관한 내용을 적는 기능
    timeSet = models.DateTimeField(default = timezone.now) # 게시글 입력 시간을 추가하는 기능
    price = models.FloatField(null = True, blank = True, default = None) # 책의 가격을 입력하는 기능
    #choices는 책의 평점을 주는 기능을 추가하는 것
    #변수 하나를 지정해서 이중 튜플로 만들면 첫번째 내용은 DB에, 두번째 내용은 admin과 form에 표시된다.
    bscore = (('first','star score 1'),
                ('second','star score 2'),
                ('third','star score 3'),
                ('fourth','star score 4'),
                ('fifth','star score 5'),
    )
    score = models.CharField(max_length = 100, choices = bscore)
    #CharField에서 해당하는 값을 설정하면 된다.
    def __str__(self):
        return self.title
