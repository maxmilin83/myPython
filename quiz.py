class Question:

    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

class QuizBrain():

    def __init__(self,questionList):
        self.questionList = questionList
        self.question_number = 0
        self.correct_questions = 0


    def ask_question(self):
        print(self.questionList[self.question_number].question)
        user_answer = input("True/False: ")
        if self.check_answer(user_answer,self.questionList[self.question_number].answer):
            self.correct_questions+=1
            self.question_number+=1
            print("Correct!")
            
        else:
            print("Incorrect!")
            self.question_number+=1
        print(f"Currenct score: {self.correct_questions}/{self.question_number}")


    def check_answer(self,user_answer,correct_answer):
        return user_answer.lower() == correct_answer.lower()

    
    def is_more_questions(self):
        return self.question_number < len(self.questionList)

    
