import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random


df = pd.read_excel('questions.xlsx')


questions = df.sample(n=3).values.tolist()


score = 0
current_question = 0


def check_answer(answer):
   global score, current_question


   if answer == correct_answer.get():
       score+=1


       current_question +=1


       if current_question < len(questions):
           display_question()
       else:
           pass


def display_question():
   global current_question


   if current_question >= len(questions):
       messagebox.showinfo("Fim do Quiz", "Parabéns! Você concluiu o quiz.")
       current_question = 0
       random.shuffle(questions)


   question = questions[current_question]
   question_label.config(text=question["question"])


   option1_btn.config(text=question["options"][0], command=lambda: check_answer(1))
   option2_btn.config(text=question["options"][1], command=lambda: check_answer(2))
   option3_btn.config(text=question["options"][2], command=lambda: check_answer(3))
   option4_btn.config(text=question["options"][3], command=lambda: check_answer(4))


   correct_answer.set(question["answer"])


   correct_answer.set(answer)


   def show_result():
       messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz. \n\nPontuação final: {score}/{len(questions)}")
       option1_btn.config(state=tk.DISABLED)
       option2_btn.config(state=tk.DISABLED)
       option3_btn.config(state=tk.DISABLED)
       option4_btn.config(state=tk.DISABLED)


def play_Again():
   global score, current_question
   score = 0
   current_question = 0
   random.shuffle(questions)
   option1_btn.config(state=tk.NORMAL)
   option2_btn.config(state=tk.NORMAL)
   option3_btn.config(state=tk.NORMAL)
   option4_btn.config(state=tk.NORMAL)
   play_again.pack()




janela= tk.Tk()
janela.title('Quiz Animalesco')
janela.geometry("400x450")


background_color = "#ADFF2F"
text_color = "#191970"
button_color = "#F0FFFF"
button_text_color = "#191970"


janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')


app_icon = PhotoImage(file="Sapo.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)


question_label = tk.Label(janela, text="Pergunta", wraplength=380, bg=background_color, fg=text_color, font=("Comic Sans MS", 13, "bold"))
question_label.pack(pady=20)


correct_answer = tk.IntVar()


option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Comic Sans MS", 10, "bold"))
option1_btn.pack(pady=10)


option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Comic Sans MS", 10, "bold"))
option2_btn.pack(pady=10)


option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Comic Sans MS", 10, "bold"))
option3_btn.pack(pady=10)


option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Comic Sans MS", 10, "bold"))
option4_btn.pack(pady=10)


play_again = tk.Button(janela, command=play_Again, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Comic Sans MS", 10, "bold"))


display_question()


janela.mainloop()

