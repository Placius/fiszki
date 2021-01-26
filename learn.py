# import modules
import os

class Learn:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = []
        self.alien_words = []
        self.last_word = 0
        self.words_quantity = 0

    def StartLearn(self):
        alien_words = []
        pl_words = []

        # download german words
        with open(str(self.lessons_language) + "/" + "alien-words.txt", "r+", encoding='utf8') as file:
            lines = file.read().split("\n")
            for line in lines:
                alien_words.append(line)

        # download polish words
        with open(str(self.lessons_language) + "/" + "pl-words.txt", "r+", encoding='utf8') as file:
                lines = file.read().split("\n")
                for line in lines:
                    pl_words.append(line)

        self.alien_words = alien_words
        self.pl_words = pl_words

        self.words_quantity = len(self.alien_words)

        while True:
            while self.last_word != self.words_quantity + 1:
                os.system('cls')
                print(self.alien_words[self.last_word], "\n")
                input("Sprawdź --> Enter")
                os.system('cls')
                print(self.alien_words[self.last_word], " <-> ", self.pl_words[self.last_word], "\n")
                choice = input("\nDalej --> Enter\nDodaj do 'Trudne' --> '1' + Enter\nDodaj do 'Już umiem' --> '2' + Enter\nPrzerwij naukę --> '3' + Enter\n-->  ")
                # change word index
                self.last_word += 1

                if self.last_word == self.words_quantity-1:
                    self.last_word = 0
                # add word to "Hard words list"
                if choice == '1':
                    pass
                
                # add word to "I know these words list"
                elif choice == '2':
                    pass

                elif choice == '3':
                    break
                
                else:
                    continue