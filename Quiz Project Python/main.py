from data import questions
from quiz import Question,QuizBrain

question_bank = [] 

for question in questions:
    questionObject = Question(question['text'],question['answer'])
    question_bank.append(questionObject)

quiz = QuizBrain(question_bank)
playAgain = "yes"

while playAgain == "yes":
    while quiz.is_more_questions():
        quiz.ask_question()
        print("\n")

    print(f"Final Score: {quiz.correct_questions}/{quiz.question_number}")
    
    playAgain = input("Play again? (yes/no): ")
    playAgain = playAgain.lower()
    if playAgain == "yes":
        quiz = QuizBrain(question_bank)
        continue
    else:
        break


