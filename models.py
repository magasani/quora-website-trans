from django.db import models

class User(models.Model):
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
'''
    def __str__(self):
        return str(self.user_name)'''

class Question(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_que')
    question = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
'''    def __str__(self):
        return str(self.question)'''

class Answer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_ans')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answer_que')
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
'''    def __str__(self):
        return str(self.answer)'''

class Like(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count=models.IntegerField(max_length=200)
'''    def __str__(self):
        return str(self.like_count)'''

