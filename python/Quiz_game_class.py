class Quiz:
  def __init__(self):
     self.questions = [
        {"quiz": "What is 1 + 1 ?", "answer": "A"},
        {"quiz": "What is 4 - 4?", "answer": "B"}
        ]
     self.choices = [
        ["A. 2", "B. 4", "C. 30", "D. 3"],
        ["A. 8", "B. 0", "C. 7", "D. 9"]
        ]

class Score:
    def __init__(self, quiz):
        self.quiz = quiz
        self.score = 0

    def check_user_answer(self, user_answer, correct_answer):
        return user_answer == correct_answer

    def play_quiz(self):
        for q_no in range(len(self.quiz.questions)):
            print(self.quiz.questions[q_no]["quiz"])

            for ans in self.quiz.choices[q_no]:
                print(ans)

            user_answer = input("Enter your answer either (A, B, C, D): ").upper()

            correct = self.check_user_answer(user_answer, self.quiz.questions[q_no]["answer"])
            if correct:
                print("Correct answer")
                self.score += 1
            else:
                print("Incorrect answer!")
                print(f'The correct answer is {self.quiz.questions[q_no]["answer"]}')
            print(f"Your current score is {self.score}/{q_no + 1}\n")

    def display_score(self):
        print(f"You have {self.score} correct answers")
        print(f"Your score is {(self.score / len(self.quiz.questions)) * 100}%")

if __name__ == "__main__":
    print("*" * 45)
    print("Welcome to Diana's Quiz Game:")
    print("*" * 45)

    quiz_game = Quiz()
    score_board = Score(quiz_game)

    score_board.play_quiz()
    score_board.display_score()
