print("*" * 35)
print("Welcome to Dianas Quiz Game:")
print("*" * 35)

question = [
  {"quiz": "What is 1 + 1 ?", "answer": "A"},
  {"quiz": "2. What is 4 - 4?", "answer": "B"}
]

choices = [
  ["A. 2", "B. 4", "C. 30", "D. 3"],
  ["A. 8", "B. 0", "C. 7", "D. 9"]
]

score = 0
def check_user_answer(user_answer, correct_answer):
  if user_answer == correct_answer:
    return True
  else:
      return False


for q_no in range(len(question)):
  print(question[q_no]["quiz"])

  for ans in choices[q_no]:
    print(ans)

  user_answer = input("Enter your answer either (A, B, C, D): ").upper()

  correct = check_user_answer(user_answer, question[q_no]["answer"])
  if correct:
    print("Correct answer")
    score += 1
  else:
    print("Incorrect answer!")
    print(f'The correct answer is {question[q_no]["answer"]}')
  print(f"Your current score is {score}/{q_no + 1}")

print(f"Your have {score} answers")
print(f"Your score is {(score/len(question))*100}%")
