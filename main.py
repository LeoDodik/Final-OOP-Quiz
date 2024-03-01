from question_model import Question
from data import question_data

question_bank = []


for question in question_data:
    just_question = question['text']
    just_answer = question['answer']
    new_question = Question(just_question,just_answer)
    question_bank.append(new_question)
