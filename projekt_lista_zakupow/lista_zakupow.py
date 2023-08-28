import os
class Lista_zakupow:
    def __init__(self):
        pass

    def menu(self):
        while True:
            
            print("To jest lista zakupow")
            print("1. Utworz liste")
            print("2. Edytuj istniejaca liste")
            print("3. Wyswietlanie istniejacej listy")
            print("4. Usun liste")
            print("5. zakoncz") 


            menu_choice = input("wybierz opcje")
            if menu_choice == "1":
                self.tworzenie_listy()
            elif menu_choice == "2":
                self.edytowanie()
            elif menu_choice == "3":
                self.wyswietlanie()
            elif menu_choice == "4":
                self.usuwanie()
            elif menu_choice == "5":
                print("elo")
                break
            else: 
                print("podaj prawidlowy wybor")

    def tworzenie_listy(self):
        try:
            file_name = input("nazwa listy zakupow")
            with open(file_name, "w", encoding="utf-8") as my_file:
                tresc = input("Podaj produkty, ktore chcesz zapisac:")
                my_file.write(tresc)
                print(f"plik {file_name} zostal utworzony")
        except Exception as e:
            print("wystapil blad: ", e)
                
    def edytowanie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        print("lista utworzonych plikow to: ")
        for file in file_list:
            print(file)
        print("wybierz plik do edycji:")
        file_name = input("podaj nazwe pliku do otwarcia")
        try:
            with open(file_name, "r+", encoding='utf-8') as my_file:
                content = my_file.read()
                print("zawartosc pliku")
                print(content)
        except FileNotFoundError:
            print("podaj poprawna nazwe pliku")
        except Exception as e:
            print("wystapil blad", e)
    def usuwanie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        print("Lista utworzonych plikow to:", file_list)
        file_delete = input("wybierz plik do usuniecia")
        if file_delete in file_list:
            os.remove(file_delete)
            print(f"plik {file_delete} zostal usuniety ")
        else:
            print(f"podany plik :{file_delete} nie istnieje. Sprawdz nazwe pliku")
    def wyswietlanie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        print("lista utworzonych plikow to:", file_list) 
        file_name = input("podaj nazwe pliku ktory chcesz wyswietlic:")
        if file_name in file_list:
            try:
                with open(file_name,'r', encoding='utf-8') as my_file:
                    content = my_file.read()
                    lines = content.split(" ")
                    for line in lines:
                        print(line)
            except Exception as e:
                print("wystapil blad: ", e) 
        else:
            print(f"podany plik o nazwie {file_name} nie istnieje. Podaj poprawna nazwe pliku")


projekt_lista = Lista_zakupow()
projekt_lista.menu()