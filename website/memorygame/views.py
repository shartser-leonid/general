import numpy as np
from django.shortcuts import render,render_to_response
from .forms import *
from .models import User,ServerLog,UserMemoryQuestionHistory,Question,QuestionLog,QuestionStatus,QuestionEvent,FixedQuestion
from django.http import HttpResponse,HttpRequest,Http404
from memorygame.gamelogic import MemoryLogic,MemoryLogicConfig,UserSession,MathGameConfig,MathGameLogic,MathAdditionProblemGenerator,MathMultProblemGenerator,MathDivProblemGenerator,MathTimeProblemGenerator,QuestionSource,FixedQuestionLogic
import jsons
from datetime import datetime

#generator_set = [MathAdditionProblemGenerator,MathMultProblemGenerator,MathDivProblemGenerator,MathTimeProblemGenerator]
generator_set = [MathTimeProblemGenerator]
mlconfig = MemoryLogicConfig(2)
mtconfig = MathGameConfig(generator_set)

#ml = [MemoryLogic(mlconfig),MathGameLogic(mtconfig)]
#ml = [MathGameLogic(mtconfig)]
ml = [FixedQuestionLogic(QuestionSource())]
def index(request):
    context={}
    return render1(request, 'memorygame/index.html', context)

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
        return HttpResponse( "Not logged in!")
    user = User.objects.get(id=user_session.user_id)
    return user

def get_question(question_id):
    try:
        user = Question.objects.get(id=int(float(question_id)))
    except:
        raise Exception(question_id)

    return user


def user_session(request):
    ServerLog.add_message('user')
    user_session = get_session(request)
    if not user_session: 
        return HttpResponse( "Not logged in!")
    #','.join(user_session.viewed_questions
    
    qq=UserMemoryQuestionHistory.objects.order_by('time_stamp').filter(user_id=user_session.user_id)
    qq = UserMemoryQuestionHistory.get_for_date(user_session.user_id,datetime.now())

    context={'user_name' : user_session.user_name, 'question_list':qq,'question_list1':user_session.viewed_questions }
    return render1(request,'memorygame/user_session.html',context)

def server(request):
    ServerLog.add_message('server')
    d=ServerLog.get_all()
    d={x.time_stamp:x.message for x in d}
    context={'server' : list(zip(d.keys(),d.values())) }
    return render1(request,'memorygame/server.html',context)

# question presented here
def question(request):
    ServerLog.add_message('question')
    user_session = get_session(request)
    if not user_session: 
        return HttpResponse( "Not logged in!")

    user = get_user(request)
    # question created
    question_str,question_voice,ans_str,instructions = np.random.choice(ml).get_random_string()
    openStatus = QuestionStatus.OPENED
    question = Question.create(question_str,openStatus)
    question.save()
    question_id=question.id


    # assign to user
    questionlog = QuestionLog.create(question,QuestionEvent.ASSIGNED,user)
    questionlog.save()

    form = QuestionForm(\
        initial={'question': question_str,\
             'correct_answer':ans_str,'question_id' : question_id}, auto_id=False)
    user_session.viewed_questions.append(question_str)
    request.session['user_id']= user_session.json

    # save question to DB

    return render1(request,'memorygame/question_display.html',\
        {'form':form,'question':question_str,'question_voice':question_voice,\
            'question_instructions':instructions,
            'question_id':question_id})

def question_answer(request):
    ServerLog.add_message('question_answer')
    user_session = get_session(request)
    if not user_session: 
        return HttpResponse( "Not logged in!")

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
    user_session.viewed_questions.append(question_str)
    request.session['user_id']= user_session.json

    # save question to DB
    return render1(request,'memorygame/question_answer.html',{'form':form})

    
def question_process(request):
    r=request.POST
    correct_answer = r['correct_answer']
    user_answer = r['answer']
    result = 'Correct!' if str(correct_answer).lower()==str(user_answer).lower() else 'Wrong.' 
    context = {'temp':[user_answer,correct_answer],'result' : result,\
        'message':"Question was: {1}. Correct answer is {2} your answer was {0}".format(user_answer,\
            r['question'],correct_answer)}
    h=UserMemoryQuestionHistory()
    h.user = get_user(request)
    h.question = r['question']
    h.was_correct = result == 'Correct!'
    h.user_answer = user_answer
    h.save()

    #get quesiton
    question = get_question(r['question_id'])
    # log answering
    questionlog = QuestionLog.create(question,QuestionEvent.ANSWERED,h.user)
    questionlog.save()

    return render1(request,'memorygame/question_answered.html',context)
    
def render1(request,url,context):
    html = render(request,url,context)
    return add_fixed_content(request,html)
    

def test2(request):
    html1="<script src='https://code.responsivevoice.org/responsivevoice.js'+';'></script>"
    html2="<script>responsiveVoice.speak('Thank you!');</script>" 
    html3="<script>responsiveVoice.speak('Wilokomen!');</script>" 
    return HttpResponse(html1+html2+html3+html2)

def chain_responses(r):
    h=''
    for html in r:
        h += html.content.decode()
    return HttpResponse(h)

def test(request):
    r=request
    
    return test2(r)
    #return chain_responses ([test2(r),test2(r)])

def add_fixed_content(request,response):
    html = response
    html = html.content.decode()
    return render(request,'memorygame/wrap_html.html',\
        {'source':html})

def login_screen(request):
    if request.method == 'POST':
        form = UserLoginForm()
        return render1(request,'memorygame/login.html',{'form':form})
    return HttpResponse( "Sorry buddy, you can't login like that, do it via homepage.")


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
                return HttpResponse( m.user_name+' already logged in, please go on.')
            request.session['user_id'] = UserSession(m.user_name,m.id).json#.toJSON()
            return HttpResponse( "Wellcome "+m.user_name+'!')
        else: 
            return HttpResponse( "Not registered user "+ru)

    return HttpResponse( "Sorry buddy, you can't login like that, do it via homepage.")

def logout(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return HttpResponse( "Not logged in!")
        user_session = UserSession.from_json(request.session['user_id'])#jsons.default_object_deserializer(request.session['user_id'],UserSession)
        context={'user_name' : user_session.user_name, }
        del request.session['user_id']
        return HttpResponse( "Bye Bye "+user_session.user_name+'!')
    return HttpResponse( "Sorry buddy, you can't logout like that, do it via homepage")