from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Some Question", fill=THEME_COLOR,
            font=("Arial", 20, "italic"), width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img,command=self.is_question_right)
        self.true_button.grid(row=2, column=0)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img,command=self.is_question_wrong)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def is_question_right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_question_wrong(self):
         self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)

