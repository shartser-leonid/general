import numpy as np
from django.shortcuts import render,render_to_response
from .forms import *
from .models import User,ServerLog,UserMemoryQuestionHistory,Question,QuestionLog,QuestionStatus,QuestionEvent,FixedQuestion
from .models import AssignedProgram,AssignedProgramCategory,AssignedProgramUser,UserActiveProgramContext
from .models import ProgramStatus,QuestionCategory
from django.http import HttpResponse,HttpRequest,Http404
from memorygame.gamelogic import MemoryLogic,MemoryLogicConfig,UserSession,MathGameConfig,MathGameLogic,MathAdditionProblemGenerator,MathMultProblemGenerator,MathDivProblemGenerator,MathTimeProblemGenerator,QuestionSourceAll,FixedQuestionLogic,QuestionSourceCategory
import jsons
from datetime import datetime
from django.db.models import Q



def get_session(request):
    if 'user_id' not in request.session:
        return None
    try:
        user_session=UserSession.from_json(request.session['user_id'])
    except:
        del request.session['user_id']
        return None
    return user_session
    
def get_user(request):
    user_session = get_session(request)
    if not user_session: 
        return render1(request,"Not logged in!",{},True)
    user = User.objects.get(id=user_session.user_id)
    return user



