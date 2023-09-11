import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

class Projekt:
    def __init__(self) -> None:
        pass
    def otwieranie(self):
        file_list = [file for file in os.listdir() if os.path.isfile(file)]
        for file in file_list:
            print(file)
        choice = input("Podaj nazwe pliku, ktory chcesz otworzyc")
        if choice in file_list:
            df = pd.read_csv(choice)
            return df
        else:
            print("Plik o podanej nazwie nie istnieje. ")
            return None


    def wyswietla(self, df):
        df_head = df.head()
        print(df_head)
        print(df_head.describe())
        print(" Co dalej?")
    
    def korelacja(self, df):
        try: 
            numeric_columns = df.select_dtypes(include=[np.number])
            if not numeric_columns.empty:
                corelationchoice = input("podaj opcje korelacji:\n1. metoda pearson\n2. metoda Matthews\n3. metoda Kendall\n4. metoda Spearman\nwybierz: ")
            
                if corelationchoice == "1":
                    result = numeric_columns.corr(method='pearson')
                elif corelationchoice == "2":
                    result = numeric_columns.corr(method='matthews')
                elif corelationchoice == "3":
                    result = numeric_columns.corr(method='kendall')
                elif corelationchoice == "4":
                    result = numeric_columns.corr(method='spearman')
                else: 
                    print("bledny wybor. Wybierz poprawny:")
                    return
                print(result)
        except ValueError as e:
            print(f'An error occured: {e}')
            
    def wykresy(self,df): 
        tytul = input("podaj tytul wykresu:")
        osx = input("podaj nazwe osi X:")
        osy = input("podaj nazwe osi Y:")
        plt.scatter(df[osx], df[osy])
        plt.xlabel(osx)
        plt.ylabel(osy)
        plt.title(f'zaleznosc miedzy{osx}, a {osy}:')
        plt.show()

    def menu(self):
        df = None
        while True:
            print("wybierz, co chcesz zrobic")
            print("1. Otwieranie pliku: ")
            print("2. wyswietlanie poczatkowe kolumny + funkcja describe()")
            print("3. wyswietlanie wykresow z kolumn")
            print("4. Korelacja")
            print("5. zakonczenie") 

            menu_choice = input("wybierz Opcje:") 

            if menu_choice == "1":
                df = self.otwieranie()
            elif menu_choice == "2": 
                if df is not None:
                    self.wyswietla(df)
                else:
                    print("nie wczytano poprawnego pliku")
            elif menu_choice == "3":
                if df is not None:
                    self.wykresy(df)
                else:
                    print('nie wczytano poprawnego pliku')
            elif menu_choice == "4":
                if df is not None:
                    self.korelacja(df)
                else:
                    print("Nie wczytano poprawnego pliku")
            elif menu_choice == "5":
                print("program zakonczony pomyslnie :)")
                break  
            else: 
                print("niepoprawny wybor. Wybierz prawildowa opcje : ")
meine_projekt = Projekt()
meine_projekt.menu()