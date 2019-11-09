from django.contrib import admin

# Register your models here.
from .models import User,UserMemoryQuestionHistory,UserProfileInfo,UserLogAction,UserLog

models = [User,UserMemoryQuestionHistory,UserProfileInfo,UserLogAction,UserLog]
for x in models: 
    admin.site.register(x)