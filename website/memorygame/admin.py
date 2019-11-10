from django.contrib import admin

# Register your models here.
from .models import User,UserMemoryQuestionHistory,UserProfileInfo,UserLogAction,UserLog,FixedQuestion

models = [User,UserMemoryQuestionHistory,UserProfileInfo,UserLogAction,UserLog,FixedQuestion]
for x in models: 
    admin.site.register(x)