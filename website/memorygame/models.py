from django.db import models
from datetime import datetime
from django.db.models import Q
from enum import Enum

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

class QuestionCategory(Enum):
    GENERAL = "GENERAL"
    MATH = "MATH"
    MEMORY = "MEMORY"
    GEOGRAPHY = "GEOGRAPHY"
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class FixedQuestion(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=QuestionCategory.choices()) 


class QuestionStatus(Enum):
    OPENED = "OPENED"
    EXPIRED = "EXPIRED"
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class QuestionEvent(Enum):
    ASSIGNED = "ASSIGNED_TO_USER"
    ANSWERING = "ANSWERING"
    ANSWERED = "ANSWERED"
    EXPIRED = "EXPIRED"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)



class Question(models.Model):
    question = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,choices=QuestionStatus.choices()) 
    
    @classmethod
    def create(cls,q,s):
        question = cls(question=q,status=s)
        return question

class QuestionLog(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    assigned_to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200,choices=QuestionEvent.choices())
    
    @classmethod
    def create(cls,q,s,user):
        questionLog = cls(question=q,status=s,assigned_to_user=user)
        return questionLog

    @classmethod
    def add_message(cls,question,status,user):
        m = QuestionLog(question,status,user)
        m.time_stamp = datetime.now()
        m.save()


class UserMemoryQuestionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    user_answer = models.CharField(max_length=200)
    was_correct = models.BooleanField()
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return "{0} : The question was {2}.  {1} answered {3}. It was {4}".format(self.time_stamp,\
            self.user.user_name,self.question,self.user_answer,'correct :) !!!' if self.was_correct else 'wrong :( .... ')
    
    @classmethod
    def get_for_date(cls,user_id1,date):

        return UserMemoryQuestionHistory.objects.filter(time_stamp__year=date.year,\
            time_stamp__month=date.month,
            time_stamp__day=date.day).select_related().filter(user_id=user_id1)

class ServerLog(models.Model):
    time_stamp = models.DateTimeField('time stamp')
    message = models.CharField(max_length=200)
    
    @classmethod
    def add_message(cls,message):
        m = ServerLog()
        m.time_stamp = datetime.now()
        m.message = message
        m.save()
    
    @classmethod
    def get_all(cls):
        return ServerLog.objects.all()

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

class AssignedProgram(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

class AssignedProgramCategory(models.Model):
    assigned_program = models.ForeignKey(AssignedProgram, on_delete=models.CASCADE)
    number_of_questions = models.IntegerField()
    category = models.CharField(max_length=200,choices=QuestionCategory.choices()) 


class ProgramStatus(Enum):
    NEW = "NEW"
    IN_PROCESS = "IN_PROCESS"
    DONE = "DONE"
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class AssignedProgramUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(AssignedProgram, on_delete=models.CASCADE)
    status = models.CharField(max_length=200,choices=ProgramStatus.choices())

class AssignedProgramUserProgress(models.Model):
    program_user = models.ForeignKey(AssignedProgramUser, on_delete=models.CASCADE)
    user_question_history = models.ForeignKey(UserMemoryQuestionHistory, on_delete=models.CASCADE)

    
class UserActiveProgramContext(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(AssignedProgramUser, on_delete=models.CASCADE)

    @classmethod
    def create(cls,u,p):
        ctxt = cls(user=u,program=p)
        return ctxt

