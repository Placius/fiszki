# all menus functions

# import modules
import os, sys, time

class GeneralMenu:
    def __init__(self):
        self.welcome_message = "Cześć, jesteś gotowy na dzsiejszą naukę?"
        self.choices = {1 : "Rozpocznij naukę", 2 : "Wybierz język menu", 3 : "Wyjście"}
        self.actual_language = "PL"
    
    def ShowMenu(self):
        os.system("cls")
        print(self.welcome_message, "\t\t\t", self.actual_language, "\n\n")
        for key, value in self.choices.items():
            print(str(key), " - ", value)
    
    def Choices(self):
        print("\n")
        while True:
            try:
                choice = int(input("Co wybierasz? - "))
                if choice in self.choices.keys():
                    return choice
                
                else:
                    print("Błądny komunikat, spróbój ponownie.")

            except ValueError:
                print("Błądny komunikat, spróbój ponownie.")
    
    def Quit(self):
        i = 3
        for i in range(4):
            os.system("cls")
            print("Do zobaczenia wkrótce!" + i*'.')
            time.sleep(1)
            i+=1

        sys.exit(0)

class ChooseLanguageMenu(GeneralMenu):
    def __init__(self):
        self.welcome_message = "Który język na teraz?"
        self.choices = {1 : "Angielski", 2 : "Niemiecki", 3 : "Powrót do menu głównego", 4 : "Wyjście"}
        self.actual_language = "PL"

class InsideLanguageMenu(GeneralMenu):
    def __init__(self):
        self.welcome_message = "Zaczynajmy!"
        self.choices = {1 : "Fiszki - nauka", 2 : "Test - sprawdź się!", 3 : "Dodaj słówko", 4 : "Usuń słówko", 
                        5 : "Dodaj zdanie", 6 : "Usuń zdanie", 7 : "Powrót do menu", 8 : "Wyjście"}
        self.actual_language = "PL"
