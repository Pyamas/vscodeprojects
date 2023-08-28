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


moj_projekt = Projekt()
moj_projekt.tworzenie()
moj_projekt.wyswietlanie()
moj_projekt.otwieranie()