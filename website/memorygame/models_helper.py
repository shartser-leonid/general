from .models import User,ServerLog,UserMemoryQuestionHistory,Question,QuestionLog,QuestionStatus,QuestionEvent,FixedQuestion
from .models import AssignedProgram,AssignedProgramCategory,AssignedProgramUser,UserActiveProgramContext
from .models import ProgramStatus,QuestionCategory
from django.db.models import Q
from .gamelogic import get_question_generator

def get_question(question_id):
    try:
        user = Question.objects.get(id=int(float(question_id)))
    except:
        raise Exception(question_id)
    return user

def get_user_assigned_program(user):
    assigned = AssignedProgramUser.objects.filter(user_id=user.id).filter(~Q(status=ProgramStatus.DONE.value))
    return assigned

def get_user_finished_program(user):
    assigned = AssignedProgramUser.objects.filter(user_id=user.id).filter(status=ProgramStatus.DONE.value)
    return assigned

def get_program(prog_user_id):
    return AssignedProgramUser.objects.get(id=prog_user_id)

def get_program_progress(prog_user_id):
    return AssignedProgramUser.objects.get(id=prog_user_id)

def get_active_user_program(user):
    activep = UserActiveProgramContext.objects.get(user_id=user.id)
    return activep
def get_program_categories(active_user_program):
    return AssignedProgramCategory.objects.filter(assigned_program_id=active_user_program.program.program.id)

def get_question_data(program_categories):
    question_generator, question_category = get_question_generator(program_categories)
    question_str,question_voice,ans_str,instructions = question_generator[0].get_random_string()
    open_status = QuestionStatus.OPENED
    question = Question.create(question_str,open_status,ans_str,question_category)
    question.save()
    return question, question_str, ans_str, question_voice, instructions
