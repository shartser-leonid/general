from .models import User,ServerLog,UserMemoryQuestionHistory,Question,QuestionLog,QuestionStatus,QuestionEvent,FixedQuestion
from .models import AssignedProgram,AssignedProgramCategory,AssignedProgramUser,UserActiveProgramContext
from .models import ProgramStatus,QuestionCategory
from django.db.models import Q


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
