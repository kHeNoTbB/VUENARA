from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) # charField : 문자(character), 필수 인수로 max_length가 있다.
    pub_date = models.DateTimeField('date published') # DateTimeField : 날짜와 시간 필드

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 각각의 Choice가 하나의 Question에 관계됨
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 기본 값을 0으로 설정함