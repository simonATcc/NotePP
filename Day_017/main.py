from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank=[]
for data in question_data:
    question= Question(data["text"],data["answer"])
    question_bank.append(question)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")