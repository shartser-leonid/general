import numpy as np
import datetime
from jsons import JsonSerializable,KEY_TRANSFORMER_CAMELCASE,KEY_TRANSFORMER_SNAKECASE
class MemoryLogicConfig:
    def __init__(self,string_lengh):
        self.string_length = string_lengh


class MemoryLogic:
    def __init__(self,memory_logic_config):
        self.history = []
        self.string_length = memory_logic_config.string_length
    
    def get_random_string(self):
        generated = self.generate()
        ans = self.answer(generated)
        self.history.append(generated)
        instructions = 'Listen to the sequence. Arrange it in order: number first (increasing order), than letters (alphabetical order) .'
        return generated,ans,instructions

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







