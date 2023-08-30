import os 
import string 
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy
class TextAnalysis:
    def __init__(self):
        pass
    
    def show_menu(self):
        while True:
            print("Menu Analizy Tekstu:")
            print("1. Analiza częstotliwosci występowanych wyrazów")
            print("2. Analiza Sentymentu:")
            print("3. Wydobywanie informacji:")
            print("4. wyswietlanie zawartosci plikow w folderze")
            print("5. Wyjscie")

            choice = input("Wybierz opcje:")

            if choice == "1":
                self.word_frequency_analysis()
            elif choice =="2":
                self.sentiment_analysis()
            elif choice == "3":
                self.information_extraction()
            elif choice == "4":
                self.showing_files()
            elif choice == "5":
                print("Zakonczenie programu:")
                break
            else:
                print("nieprawidlowa opcja, wybierz ponownie: ")

    def word_frequency_analysis(self):
        print("Funkcja analizy częstości wyrazów: ")
        script_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_directory)
        file_name = input("Podaj nazwe pliku tekstowego do Analizy: ")
        
        try:
            with open(file_name, "r", encoding="utf-8") as file: 
                text = file.read().lower()
                words = text.split()
                words = [word.strip(string.punctuation) for word in words]

                word_count = Counter(words)
                for word, count in word_count.items():
                    if count >= 2:
                        print(f"Slowo '{word}' wystepuje {count} razy")

        except FileNotFoundError:
            print(f"Plik {file_name} nie istnieje, podaj wlasciwa nazwe pliku")
        except Exception as e:
            print("wystapil blad: ", e)
        
        
    def sentiment_analysis(self):
        print("funkcja analizy sentymentu: ")
        nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()

        text = input("podaj przykladowy tekst w jezyku ANGIELSKIM")

        lines = text.split("\n")
        for line in lines:
            sentiment_scores = sia.polarity_scores(line)
            print(line)
            print("sentiment scores:", sentiment_scores)
            print("=" * 30)
        
    def information_extraction(self):
        print("funkcja wydobywania informacji: ")
        nlp = spacy.load("pl_core_news_md")
        text = input("podaj tekst do analizy")
        doc = nlp(text)
        
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_)
        
    def showing_files(self):
        script_folder = os.path.dirname(os.path.abspath(__file__))
        file_list = [file for file in os.listdir(script_folder) if os.path.isfile(os.path.join(script_folder, file))]
        print("wyswietlanie plikow zawartych w folderze: ")
        for file in file_list:
            print(file)


text_analysis = TextAnalysis()
text_analysis.show_menu()