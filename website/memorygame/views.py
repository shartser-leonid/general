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

from .gamelogic import mark_to_letter
from .views_helpers import *
from .models_helper import *

generator_set = [MathAdditionProblemGenerator,MathMultProblemGenerator,\
    MathDivProblemGenerator,MathTimeProblemGenerator]
mlconfig = MemoryLogicConfig(2)
mtconfig = MathGameConfig(generator_set)
ml = [MemoryLogic(mlconfig),MathGameLogic(mtconfig),FixedQuestionLogic(QuestionSourceAll())]

def index(request):
    context={}
    return render1(request, 'memorygame/index.html', context)


def program_view(request):
    user_session = get_session(request)
    if not user_session: 
        return  render1(request,"Not logged in!",{},True)

    user = get_user(request)
    assigned_progs=get_user_assigned_program(user)
    finished_progs=get_user_finished_program(user)

    context={'user_name' : user_session.user_name,\
          'finished_program_list':finished_progs,\
          'assigned_program_list':assigned_progs  }
    return render1(request,'memorygame/program_view.html',context)

def program_activate(request,user_prog_id):
    user_session = get_session(request)
    if not user_session: 
        return  render1(request,"Not logged in!",{},True)

    user = get_user(request)
    program = get_program(user_prog_id)
    UserActiveProgramContext.objects.filter(user_id=user.id).delete()
    activation=UserActiveProgramContext.create(user,program)
    activation.save()

    context={'user_name' : user_session.user_name,  'program' : program.program.name }
    return render1(request,'memorygame/program_activated.html',context)


    
def program_progress(request,user_prog_id):
    user_session = get_session(request)
    if not user_session: 
        return  render1(request,"Not logged in!",{},True)

    user = get_user(request)
    program = get_program(user_prog_id)
    prgram_list = AssignedProgramCategory.objects.filter(assigned_program_id=program.program.id)

    progress_list = UserMemoryQuestionHistory.get_progres(program)
    for q in progress_list:
        percent=100*q['correct_ones']/q['question_per_category']
        q['mark'] = percent
        q['mark_l'] = mark_to_letter(percent)

    context={'program_list':prgram_list,'progress_list':progress_list}
    return render1(request,'memorygame/program_progress.html',context)


def program_report(request,prog_id):
    user_session = get_session(request)
    if not user_session: 
        return  render1(request,"Not logged in!",{},True)

    user = get_user(request)
    program = get_program(prog_id)
    assigned_progs=get_user_assigned_program(user)
    context={'user_name' : user_session.user_name,  'program' : program }
    return render1(request,'memorygame/program_report.html',context)

def user_session(request):
    ServerLog.add_message('user')
    user_session = get_session(request)
    if not user_session: 
        return  render1(request,"Not logged in!",{},True)
    
    qq=UserMemoryQuestionHistory.objects.order_by('time_stamp').filter(user_id=user_session.user_id)
    qq = UserMemoryQuestionHistory.get_for_date(user_session.user_id,datetime.now())

    context={'user_name' : user_session.user_name, 'question_list':qq}
    return render1(request,'memorygame/user_session.html',context)

def server(request):
    ServerLog.add_message('server')
    d=ServerLog.get_all()
    d={x.time_stamp:x.message for x in d}
    context={'server' : list(zip(d.keys(),d.values())) }
    return render1(request,'memorygame/server.html',context)

def get_next_question(user_program):
    # selected unfinished categories 
    pass

def log_question(request,question_text,question,user_answer,log_event, was_correct):
    user1 = get_user(request)
    questionlog = QuestionLog.create(question,log_event,user1)
    questionlog.save()

    # program progress
    active_user_program = get_active_user_program(user1)

    # user history
    h=UserMemoryQuestionHistory.objects.filter(question_log__question__id=questionlog.question.id)

    if not h:
        h=UserMemoryQuestionHistory()
    else:
        h=h[0]

    h.user = user1
    h.question_log = questionlog
    h.program_user = active_user_program.program
    h.question = question_text
    h.was_correct = was_correct
    h.user_answer = user_answer
    h.save()


# question presented here
def question(request):
    ServerLog.add_message('question')
    user_session = get_session(request)
    if not user_session: 
        return render1(request,"Not logged in!",{},True)

    user = get_user(request)

    # get active program
    p = get_active_user_program(user)
    program_goal = AssignedProgramCategory.objects.filter(assigned_program_id=p.program.program.id)
    #program_progress = AssignedProgramUserProgress.objects.filter()
    d1={x.category:x.number_of_questions for x in program_goal}
    d2={}
    for y in d1:
        if y in [x.value for x in [QuestionCategory.CANADIAN_PROVINCES,QuestionCategory.GENERAL,QuestionCategory.GEOGRAPHY]]:
            d2[y] = QuestionSourceCategory(y)

    pool=[]
    #ml = [MemoryLogic(mlconfig),MathGameLogic(mtconfig),FixedQuestionLogic(QuestionSourceAll())]
    switcher={ 'MATH' : MathGameLogic(mtconfig),'MEMORY':MemoryLogic(mlconfig)  }
    for i in d1.items():
        pool.extend( i[1]*[  (switcher[i[0]],i[0]) if i[0] in switcher else (FixedQuestionLogic(d2[i[0]]),i[0]) ])

    # get next question from the program


    # question created
    question_generator = pool[np.random.choice(len(pool))]
    question_category= question_generator[1]
   
    question_str,question_voice,ans_str,instructions = question_generator[0].get_random_string()
    open_status = QuestionStatus.OPENED
    question = Question.create(question_str,open_status,ans_str,question_category)
    question.save()
    question_id=question.id


    log_question(request,question_str,question,'No answer',QuestionEvent.ASSIGNED,0)

    form = QuestionForm(\
        initial={'question': question_str,\
                 'correct_answer':ans_str,\
                 'question_id' : question_id}, auto_id=False)
    request.session['user_id']= user_session.json

    return render1(request,'memorygame/question_display.html',\
        {'form':form,'question':question_str,'question_voice':question_voice,\
            'question_instructions':instructions,
            'question_id':question_id},wrap_html='wrap_html_question')

def question_answer(request):
    ServerLog.add_message('question_answer')
    user_session = get_session(request)
    if not user_session: 
        return   render1(request,"Not logged in!",{},True)
    r = request.POST
    user = get_user(request)
    #get quesiton
    question = get_question(r['question_id'])
    # log answering
    questionlog = QuestionLog.create(question,QuestionEvent.ANSWERING,user)
    questionlog.save()
    question_str,ans_str,question = r['question'],r['correct_answer'],r['question']
    form = AnswerForm(initial={'question':question,'answer': '', 
    'correct_answer':ans_str,'question_id' : r['question_id']}, auto_id=False)
    request.session['user_id']= user_session.json
    return render1(request,'memorygame/question_answer.html',{'form':form},\
        wrap_html='wrap_html_question')

    
def question_process(request):
    r=request.POST
    correct_answer = r['correct_answer']
    user_answer = r['answer']
    result = 'Correct!' if str(correct_answer).lower()==str(user_answer).lower() else 'Wrong.' 
    context = {'temp':[user_answer,correct_answer],'result' : result,\
        'message':"Question was: {1} The correct answer is {2} . your answer was {0} .".format(user_answer,\
            r['question'],correct_answer)}

    #get quesiton
    question = get_question(r['question_id'])
    log_question(request,r['question'],question,user_answer,QuestionEvent.ANSWERED,result == 'Correct!')
    

    return render1(request,'memorygame/question_answered.html',context)

    
def render1(request,url,context,is_html=False,wrap_html='wrap_html'):
    html = url if is_html else render(request,url,context)
    context['user_name']='No user'
    context['program']='No program'
    try:
        user=get_user(request)
        context['user_name'] = user.user_name
        context['program'] = get_active_user_program(user).program.program.name
    except:
        pass
    return add_fixed_content(request,html,context,is_html,wrap_html)
    
def add_fixed_content(request,response,context,is_html=False,wrap_html='wrap_html'):
    html = response
    if not is_html:
        html = html.content.decode()
    context['source'] = html
    return render(request,'memorygame/{}.html'.format(wrap_html),context)

def login_screen(request):
    if request.method == 'POST':
        form = UserLoginForm()
        return render1(request,'memorygame/login.html',{'form':form})
    return render1(request,"Sorry buddy, you can't login like that, do it via homepage.",{},True)


def login(request):
    if request.method == 'POST':
        ru=request.POST['user_name']
        try:
            m = User.objects.get(user_name=ru)
        except User.DoesNotExist:
            m=None
        if m:
            u = None
            if 'user_id' in request.session:
                u=UserSession.from_json(request.session['user_id'])

            if u and u.user_name==ru:
                return render1(request, m.user_name+' already logged in, please go on.',{},True)
            request.session['user_id'] = UserSession(m.user_name,m.id).json#.toJSON()
            return render1(request, "Wellcome "+m.user_name+'!',{},True)
        else: 
            return render1( request,"Not registered user "+ru,{},True)

    return render1(request,"Sorry buddy, you can't login like that, do it via homepage.",{},True)

def logout(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return  render1(request,"Not logged in!",{},True)
        user_session = UserSession.from_json(request.session['user_id'])#jsons.default_object_deserializer(request.session['user_id'],UserSession)
        context={'user_name' : user_session.user_name, }
        del request.session['user_id']
        return render1(request,"Bye Bye "+user_session.user_name+'!',{},True)
    return render1(request,"Sorry buddy, you can't logout like that, do it via homepage",{},True)