from django.db import models
from django.contrib.auth.models import User

class Answer(models.Model):
    answer_text = models.TextField(blank=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True , blank=True)
    def __str__(self):
        return self.answer_text
    
class Question(models.Model):
    QUESTION_TYPE  =(
        ('text', 'text'),
        ('photo', 'photo'),
        ('poll', 'poll')
    )
    question_text = models.TextField(blank=False) 
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    question_type = models.CharField(max_length=12,choices=QUESTION_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question_text
    
    def get_answers(self):
        ans = Answer.objects.filter(question_id = self.id).count()
        return ans
        
      
class Reaction(models.Model):
    REACTION_TYPE= (
        ('upvote', 'upvote'),
        ('downvote', 'downvote')
    )
    reaction_type = models.CharField(max_length=10 , default='upvote')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user.username + " - " +self.question.question_text)