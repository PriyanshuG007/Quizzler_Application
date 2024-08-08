from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#405D72"


class QuizzlerInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=30, pady=40)
        self.window.title("QUIZZLER APPLICATION")

        self.display_canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_test = self.display_canvas.create_text(150,
                                                             125,
                                                             width=280,
                                                             text="question",
                                                             fill=THEME_COLOR,
                                                             font=("Arial", 15, "italic")
                                                             )

        self.display_canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.score_label = Label(text="SCORE: 0", bg=THEME_COLOR, foreground="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        right_image = PhotoImage(file="true.png")
        self.right_button = Button(image=right_image, width=100, height=90, highlightthickness=0, bg=THEME_COLOR, command=self.user_chose_true)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="false.png")
        self.wrong_button = Button(image=wrong_image, width=100, height=90, highlightthickness=0, bg=THEME_COLOR, command=self.user_chose_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():

            self.display_canvas.config(bg="white")
            self.score_label.config(text=f"SCORE: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.display_canvas.itemconfig(self.question_test, text=q_text)
        else:
            self.display_canvas.config(bg="white")
            self.display_canvas.itemconfig(self.question_test, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def user_chose_true(self):
        user_answer = "True"
        actual_answer = self.quiz.check_answer(user_answer)
        self.give_feedback(actual_answer)

    def user_chose_false(self):
        user_answer = "False"
        actual_answer = self.quiz.check_answer(user_answer)
        self.give_feedback(actual_answer)

    def give_feedback(self, actual_answer):
        if actual_answer:
            self.display_canvas.config(bg="#29B677")
        else:
            self.display_canvas.config(bg="#EE665D")
        self.window.after(1000, self.get_next_question)
