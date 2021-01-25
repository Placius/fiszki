# import modules
import os

class Learn:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = []
        self.alien_words = []

    def StartLearn(self):
        alien_words = []
        pl_words = []

        # download german words
        with open(str(self.lessons_language) + "/" + "alien-words.txt", encoding='utf8') as file:
            lines = file.read().split("\n")
            for line in lines:
                alien_words.append(line)

        # download polish words
        with open(str(self.lessons_language) + "/" + "pl-words.txt", encoding='utf8') as file:
                lines = file.read().split("\n")
                for line in lines:
                    pl_words.append(line)

        self.alien_words = alien_words
        self.pl_words = pl_words

        while True:
            words_quantity = len(self.alien_words)
            last_word = 0
            while last_word != words_quantity + 1:
                os.system('cls')
                print(self.alien_words[last_word], "\n")
                input("Sprawdź --> Enter")
                os.system('cls')
                print(self.alien_words[last_word], " <-> ", self.pl_words[last_word], "\n")
                input("Dalej --> Enter")

                last_word += 1

                if last_word == words_quantity:
                    last_word = 0
                
                else:
                    continue