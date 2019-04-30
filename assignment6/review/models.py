from django.db import models
from django.utils import timezone
# Create your models here.

from imagekit.models import ImageSpecField ### Thumbnail making module
from imagekit.processors import ResizeToFill ### Thumbnail size module



class WritingContents(models.Model): #게시글 작성을 위해 DB에 입력되어야할 내용들을 추가시키는 Class
    title = models.CharField(max_length = 200, help_text = '최대 200자 입력가능') #제목 입력 기능
    contents = models.TextField() # book review에 관한 내용을 적는 기능
    timeSet = models.DateTimeField(default = timezone.now) # 게시글 입력 시간을 추가하는 기능
    price = models.FloatField(null = True, blank = True, default = None) # 책의 가격을 입력하는 기능
    #choices는 책의 평점을 주는 기능을 추가하는 것
    #변수 하나를 지정해서 이중 튜플로 만들면 첫번째 내용은 DB에, 두번째 내용은 admin과 form에 표시된다.
    bscore = ((1,'1'),
                (2,'2'),
                (3,'3'),
                (4,'4'),
                (5,'5'),
    )
    cover = models.ImageField(upload_to='images/')
    score = models.IntegerField(default = 5, choices = bscore)
    #CharField에서 해당하는 값을 설정하면 된다.
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    #On_delete는 이 댓글이 속한 포스트가 삭제 되었을 때 어떻게 할 것인가에 대한 행동 지시
    post = models.ForeignKey(WritingContents, on_delete= models.CASCADE, related_name = 'comments')
    content = models.TextField()