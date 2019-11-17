from django.contrib import admin

# Register your models here.
from .models import User,UserMemoryQuestionHistory,UserProfileInfo,UserLogAction,UserLog,FixedQuestion
from .models import AssignedProgram,AssignedProgramCategory,AssignedProgramUser

models = [User,UserMemoryQuestionHistory,UserProfileInfo,UserLogAction,UserLog,FixedQuestion,\
    AssignedProgram,AssignedProgramCategory,AssignedProgramUser]
for x in models: 
    admin.site.register(x)