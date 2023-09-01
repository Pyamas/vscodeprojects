class Question:
    def __init__(self, text, answers, correct_answer):
        self.text = text
        self.answers = answers
        self.correct_answer = correct_answer
    

class Quiz:
    def __init__(self, questions):
        self.qestions = questions
        self.score = 0

    def menu(self):
        while True: 
            print("1. Start!")
            print("2. Zakoncz!")
            print("3. Punktacja:")

            choice = input("wybierz opcje:")
        
            if choice == "1":
                print("zaczynamy!")
                self.run()
            elif choice == "2":
                print("elo")
                break 
            elif choice == "3":
                print("punktacja")
    def punktacja(self):
        question = 0 
        if user_choice.isdigit():
            user_choice = int(user_choice) -1
            if 0 <= user_choice <len(question.answers):
                if question.answers[user_choice] == question.correct_answer:
                    self.score +=1
                    print("Prawidlowa Odpowiedz!: \n")
                else:
                    print(f"Zle! prawidlowa odpowiedz to: {question.correct_answer}\n")
            else:
                print("zly wybor!\n ")
        else:
            print("nieprawidlowe wprowadzenie\n")
        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")
    def run(self):
        for i, question in enumerate(self.questions, start=1):
            print(f'Question {i}: {question.text}')
            for j, answer in enumerate(question.answers, start=1):
                print(f"{j}. {answer}")
        user_choice = input("Podaj odpowiedz!: ")
        self.punktacja()
    questions = [
        Question("Jaka jest stolica Francji?" ,["Paryz"," Madryt", "Berlin"], "Paryz"),
        Question("Jaka planeta jest znana jako czerwona planeta? ",["Ziemia","Mars","Venus"], "Mars")
        
    ]

quiz = Quiz(questions)
quiz.run()