class Calculator():
    def __init__(self) -> None:
        pass
    def men(self):
        while True: 
            print("co chcesz  zrobic?")
            print("1. dodawanie")
            print("2. mnozenie")
            print("3. dzielenie")
            print("4. zakoncz") 

            menu_choicee = input("wybierz opcje: ")

            if menu_choicee == "1":
                self.dodawanie()
            elif menu_choicee =="2":
                self.mnozenie()
            elif menu_choicee =="3":
                self.dzielenie()
            elif menu_choicee =="4":
                print("elo")
                break
            else:
                print("niepoprawny wybor. Wybierz odpowiednia opcje.")

    
    def dodawanie(self):
        while True: 
            try:
                ilosc_liczb = int(input("Ile liczb chcesz dodac?" ))
                if ilosc_liczb in range(1,11):
                    suma = 0 
                    for _ in range(ilosc_liczb):
                        liczba = float(input("podaj liczbe: "))
                        suma += liczba
                    print("suma podanych liczb wynosi: ", suma) 
                    break
                else: 
                    print("podaj liczbe z zakresu od 1 do 10: ")
            except ValueError:
                print("nieprawidlowy format liczby. Podaj liczbe calkowita.")
            
            
            
    def mnozenie(self): 
        while True:
            try: 
                ilosc = int(input("ile liczb chcesz pomnozyc?"))
                if ilosc in range(1,11):
                    iloczyn = 1
                    for _ in range(ilosc):
                        liczba1 = float(input("podaj liczbe" ))
                        iloczyn  *= liczba1
                    print("iloczyn podanych liczb wynosi: ", iloczyn)
                    break
                else:
                    print("podaj liczbe z zakresu od 1 do 10: ")
            except ValueError:
                print("niepoprawny format liczby, podaj liczbe calkowita:") 
    def dzielenie(self):
        while True:
            try:
                ile = int(input("ile liczb chcesz podzielic?"))
                if ile in range(1,11):
                    iloraz = None
                    for _ in range(ile):
                        liczba2 = float(input("podaj liczbe"))
                        if iloraz is None:
                            iloraz = liczba2
                        elif liczba2 != 0:
                            iloraz /= liczba2 
                        else: 
                            print("nie mozna dzielic przez 0") 
                    if iloraz is not None:
                        print("iloraz podanych lcizb wynosi:", iloraz)
                    break 
                else: 
                    print("podaj liczbe z zakresu od 1 do 10:") 
            except ValueError:
                print("niepoprawny format liczby. Podaj liczbe poprawna")

projekt_kalkulator = Calculator()
projekt_kalkulator.men()
#projekt_kalkulator.dodawanie()
#projekt_kalkulator.mnozenie()
#projekt_kalkulator.dzielenie()
