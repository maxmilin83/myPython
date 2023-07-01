from data import questions
from quiz import Question

question_bank = [] 

for question in questions:
    questionObject = Question(question['text'],question['answer'])
    question_bank.append(questionObject)

