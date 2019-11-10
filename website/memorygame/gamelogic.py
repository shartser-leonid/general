import numpy as np
import datetime
from jsons import JsonSerializable,KEY_TRANSFORMER_CAMELCASE,KEY_TRANSFORMER_SNAKECASE
from enum import Enum
from datetime import timedelta
from random import randrange

class MemoryLogicConfig:
    def __init__(self,string_lengh):
        self.string_length = string_lengh

class MathGameConfig:
    def __init__(self,question_generators):
        self.question_generators = question_generators


class MathAdditionProblem:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def generate(self):
        return "Solve the additon problem: {} + {} = ?".format(self.a,self.b)
    def instructions(self):
        return "Solve the additon problem: {} + {} = ?".format(self.a,self.b)
    def solution(self):
        return self.a+self.b

class MathMultProblem:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def generate(self):
        return "Solve the multiplication problem: {} x {} = ?".format(self.a,self.b)
    def instructions(self):
        return "Solve the multiplication problem: {} x {} = ?".format(self.a,self.b)
    def solution(self):
        return self.a*self.b

class MathDivProblem:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def generate(self):
        return "Solve the division problem: {} : {} = ?".format(self.a*self.b,self.a)
    def instructions(self):
        return "Solve the division problem: {} : {} = ?".format(self.a*self.b,self.a)
    def solution(self):
        return self.b

class TimeDelta:
    def __init__(self,days,hours,minutes):
        self.days,self.hours,self.minutes=days,hours,minutes
    def __str__(self):
        return "{} hours {} minutes".format(self.hours,self.minutes)

class TimeDeltaFactory:
    @classmethod
    def create(cls,d,h,m):
        return TimeDelta(np.random.randint(d),np.random.randint(h),np.random.randint(m))

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

class MathTimeProblem:
    def __init__(self,base_time,operation,delta_time):
        self.base_time = base_time
        self.operation = operation
        self.delta_time = delta_time
    
    class Operations(Enum):
        ADD='Add'
        SUB='Sub'

    def display(self,td):
        return 
    def generate(self):
        op = self.operation
        if op==MathTimeProblem.Operations.ADD:
            return "Now it is {:02d}:{:02d}. What time time WILL be in {} ?".format(self.base_time.hour,self.base_time.minute,self.delta_time)
        if op==MathTimeProblem.Operations.SUB:
            return "Now it is {:02d}:{:02d}. What time time WAS {} ago ?".format(self.base_time.hour,self.base_time.minute,self.delta_time)
    def instructions(self):
        return self.generate()
    
    def solution(self):
        op = self.operation
        td = self.delta_time
        if op==MathTimeProblem.Operations.ADD:
           ans=self.base_time + timedelta(days=td.days,minutes=td.minutes,hours=td.hours)  
        if op==MathTimeProblem.Operations.SUB:
            ans=self.base_time - timedelta(days=td.days,minutes=td.minutes,hours=td.hours)  
        return "{:02d}:{:02d}".format(ans.hour,ans.minute)    

class DisplayProblem:
    def __init__(self,question_voice,question_text,question_instructions):
        self.question_voice,self.question_text,self.question_instructions=question_voice,question_text,question_instructions

class MathAdditionProblemGenerator:
    def generate(self):
        return MathAdditionProblem(np.random.randint(1000),np.random.randint(1000))

class MathMultProblemGenerator:
    def generate(self):
        return MathMultProblem(np.random.randint(10),np.random.randint(10))

class MathDivProblemGenerator:
    def generate(self):
        return MathDivProblem(1+np.random.randint(10),np.random.randint(10))

class MathTimeProblemGenerator:
    def generate(self):
        d1 = datetime.datetime.strptime('1/1/1990 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.datetime.strptime('1/1/2050 4:50 AM', '%m/%d/%Y %I:%M %p')

        basedate=random_date(d1, d2)

        return MathTimeProblem(basedate,np.random.choice(MathTimeProblem.Operations),TimeDeltaFactory.create(10,13,61))


class MathGameLogic:
    def __init__(self,math_game_config):
        self.question_generators = math_game_config.question_generators

    def get_random_string(self):
        generated = self.generate()
        instructions = generated.instructions()
        return generated.generate(),'',generated.solution(),instructions

    def generate(self):
        gen = np.random.choice(self.question_generators)
        return gen().generate()



class MemoryLogic:
    def __init__(self,memory_logic_config):
        self.string_length = memory_logic_config.string_length
    
    def get_random_string(self):
        question_voice = self.generate()
        question_text = "Arrange the sequence "+question_voice
        ans = self.answer(question_voice)
        instructions = 'Listen to the sequence. Arrange it in order: number first (increasing order), than letters (alphabetical order) .'
        return question_text,question_voice, ans,instructions

    def answer(self,quest):
        return "".join(sorted(quest))    

    def generate(self):
        letters = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        digits = set(list('0123456789'))
        sequence = ''
        for i in range(self.string_length):
            c = np.random.choice(list(letters))
            n = np.random.choice(list(digits))
            sequence +=c
            sequence +=str(n)
            letters.remove(c)
            digits.remove(n)
        return sequence

class UserSession(JsonSerializable
              .with_dump(key_transformer=KEY_TRANSFORMER_CAMELCASE)
              .with_load(key_transformer=KEY_TRANSFORMER_SNAKECASE)):
    def __init__(self,user_name : str, user_id : int ):
        self.user_name = user_name
        self.user_id = user_id
        self.viewed_questions = []
        self.answers = {} # question -> answer
        self.number_of_correct_answers = 0
        self.login_time = datetime.datetime.now()







