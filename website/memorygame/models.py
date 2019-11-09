from django.db import models
from datetime import datetime
from django.db.models import Q

'''
class MemoryQuestion(models.Model):
    question_text = 'Remember the following sequence\n {}. Please type in separtely the numbers in ascending order and letters in alphabetical order.'
    question_data = models.CharField(max_length=200)
    question_correct_answer = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
'''

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    time_stamp = models.DateTimeField('time stamp')

class UserLogAction(models.Model):
    action = models.CharField(max_length=200) # login,logout,etc

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.ForeignKey(UserLogAction, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    time_stamp = models.DateTimeField('time stamp')


class UserMemoryQuestionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    user_answer = models.CharField(max_length=200)
    was_correct = models.BooleanField()
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return "{0} : The question was {2}.  {1} answered {3}. It was {4}".format(self.time_stamp,\
            self.user.user_name,self.question,self.user_answer,'correct :) !!!' if self.was_correct else 'wrong :( .... ')
    def get_for_date(user_id1,date):

        return UserMemoryQuestionHistory.objects.filter(time_stamp__year=date.year,\
            time_stamp__month=date.month,
            time_stamp__day=date.day).select_related().filter(user_id=user_id1)

class ServerLog(models.Model):
    time_stamp = models.DateTimeField('time stamp')
    message = models.CharField(max_length=200)
    def add_message(message):
        m = ServerLog()
        m.time_stamp = datetime.now()
        m.message = message
        m.save()
    def get_all():
        return ServerLog.objects.all()


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username