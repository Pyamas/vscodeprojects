import os
class Lista_zakupow:
    def __init__(self):
        pass

    def menu(self):
        while True:
            
            print("To jest lista zakupow")
            print("1. Utworz liste")
            print("2. Edytuj istniejaca liste")
            print("3. Usun liste")

            menu_choice = input("wybierz opcje")
            if menu_choice == "1":
                self.tworzenie_listy()
            if menu_choice == "2":
                self.edytowanie()
            if menu_choice == "3":
                self.usuwanie()
            else:
                print("podaj prawidlowy wybor")

    def tworzenie_listy(self):
        file_name = str(input("nazwa listy zakupow"))
        with open(file_name, "w", encoding="utf-8") as my_file:
            my_file.write("Podaj produkty, ktore chcesz zapisac:")
            for line in file_name:
                line.splitlines()
                print(my_file)
                
    def edytowanie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        print("lista utworzonych plikow to: ")
        for file in file_list:
            print(file)
        print("wybierz plik do edycji:")
        file_name = input("podaj nazwe pliku do otwarcia")
        try:
            with open(file_name, "w", encoding='utf-8') as my_file:
                content = my_file.read()
                print("zawartosc pliku")
                print(content)
        except FileNotFoundError:
            print("podaj poprawna nazwe pliku")
        except Exception as e:
            print("wystapil blad: ", e) 
    
    def usuwanie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        print("Lista utworzonych plikow to:")
        for file in file_list:
            print(file)
        file_delete = input("wybierz plik do usuniecia: ")
        os.remove(file_delete)
    

projekt_lista = Lista_zakupow()
projekt_lista.menu()