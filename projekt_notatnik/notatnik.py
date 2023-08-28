import os
class Projekt:
    def __init__(self):
        pass

    def tworzenie(self):
        file_name = input("podaj nazwe pliku:")
        try:
            with open(file_name, 'w', encoding = 'utf-8') as my_file:
                my_file.write(input("co chcesz napisac?"))
            print("plik zostal utworzony i zapisany")

        except Exception as e:
            print("wystapil blad: ", e)

    def otwieranie(self):
        file_name = input("podaj nazwe pliku do otwarcia: ")
        try:
            with open(file_name, 'r', encoding='utf-8') as my_file:
                content = my_file.read()
                print("zawartosc pliku")
                print(content)
        except FileNotFoundError:
            print("plik nie istnieje:")
        except Exception as e:
            print("wystapil blad:", e)
    def wyswietlanie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        print("lista utworzonych plikow to: ")
        for file in file_list:
            print(file)
    def menu(self):
        while True: 
            print("co chcesz dalej zrobic?")
            print("1. Tworzenie pliku")
            print("2. Otwieranie pliku")
            print("3. wyswietlanie listy plikow")
            print("4. zakoncz") 

            menu_choice = input("wybierz opcje: ")

            if menu_choice == "1":
                self.tworzenie()
            elif menu_choice =="2":
                self.otwieranie()
            elif menu_choice =="3":
                self.wyswietlanie()
            elif menu_choice =="4":
                print("elo")
                break
            else:
                print("niepoprawny wybor. Wybierz odpowiednia opcje.")

moj_projekt = Projekt()
moj_projekt.tworzenie()
moj_projekt.wyswietlanie()
moj_projekt.otwieranie()
moj_projekt.menu()

