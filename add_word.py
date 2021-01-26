import time, os

class NewWord:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.new_pl_word = "new pl word"
        self.new_alien_word = "new alien word"
    
    def AddWord(self):
        while True:
            os.system("cls")
            print("Jeśli chcesz powrócić do menu wprowadź komunikat 'elo' po czym wciśnij Enter.\n\n")
            if self.lessons_language == "deutsch":
                print("Przydatne znaki: ä  Ä  ö  Ö  ü  Ü  ß\n\n")

            self.new_alien_word = input("Wpisz nowe słówko: ")
            if self.new_alien_word == "elo":
                break

            else:
                self.new_pl_word = input("Polskie znaczenie: ")

            try:
                with open(str(self.lessons_language) + "/" + "alien-words.txt", "a+", encoding='utf8') as file:
                    file.write(self.new_alien_word + "\n")

                with open(str(self.lessons_language) + "/" + "pl-words.txt", "a+", encoding='utf8') as file:
                    file.write(self.new_pl_word + "\n")
                
                print("Słówko zostało poprawnie dodatne.")
                time.sleep(3)
            
            except FileNotFoundError:
                print("Nie można odnaleźć plików z listami słowek...")