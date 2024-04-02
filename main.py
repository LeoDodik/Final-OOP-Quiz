
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Fetch questions from question_data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize QuizBrain and QuizInterface
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# Run the quiz loop
while quiz.still_has_questions():
    quiz.next_question()

# Once the quiz is completed, print the final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []


for question in question_data:
    just_question = question['text']
    just_answer = question['answer']
    new_question = Question(just_question,just_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()



while quiz.still_has_questions():
    quiz.next_question()
if quiz.still_has_questions() == False:
    print("You've completed the quiz")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")



