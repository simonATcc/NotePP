#TODO:asking the queestion
#TODO:check the answer is correct
#TODO: checking if we're the end of the quiz
class QuizBrain:
    def __init__(self,question_list) -> None:
        self.question_number=0
        self.question_list=question_list
        self.score=0
    def next_question(self):
        quiz=self.question_list[self.question_number]
        answer=input(f"Q{self.question_number}:{quiz.text} (True/False)?")
        self.question_number+=1
        self.check_answer(answer,quiz.answer)
    def still_has_questions(self):
        return self.question_number< len(self.question_list)
    def check_answer(self,user_answer:str,correct_answer:str):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")