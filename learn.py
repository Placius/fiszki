# import modules
import os, time
import words_segreagtor

class Learn:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = []
        self.alien_words = []
        self.last_word = 0
        self.words_quantity = 0
        self.segregator_words = []

        self.DownloadWordsLists()
    
    def DownloadWordsLists(self):
        alien_words = []
        pl_words = []

        # download alien words
        with open(str(self.lessons_language) + "/" + "alien-words.txt", "r+", encoding='utf8') as file:
            lines = file.read().split("\n")
            for line in lines:
                if len(line) > 0:
                    alien_words.append(line)
                else:
                        continue

        # download polish words
        with open(str(self.lessons_language) + "/" + "pl-words.txt", "r+", encoding='utf8') as file:
                lines = file.read().split("\n")
                for line in lines:
                    if len(line) > 0:
                        pl_words.append(line)
                    else:
                        continue

        self.alien_words = alien_words
        self.pl_words = pl_words
    
    def DownloadKnow_HardWordsLists(self, list):
        # download actual know words list
            lista = []
            with open(str(self.lessons_language) + "/" + str(list) + ".txt", "r+", encoding='utf8') as file:
                lines = file.read().split("\n")
                for line in lines:
                    if len(line) > 0:
                        lista.append(line)
                    else:
                        continue
            self.segregator_words = lista

    def StartLearn(self):
        self.words_quantity = len(self.alien_words)

        
        while True:
            os.system('cls')
            print("\t\t\t\t\t", self.alien_words[self.last_word], "\n")
            input("Sprawdź --> Enter")
            os.system('cls')
            print("\t\t\t\t\t", self.alien_words[self.last_word], " <-> ", self.pl_words[self.last_word], "\n")
            choice = input("\nDalej --> Enter\nDodaj do 'Trudne' --> '1' + Enter\nDodaj do 'Już umiem' --> '2' + Enter\nPrzerwij naukę --> '3' + Enter\n-->  ")

            # add word to "Hard words list"
            if choice == '1':
                self.DownloadKnow_HardWordsLists("hard_words")
                if self.alien_words[self.last_word] in self.segregator_words:
                    print("Słówko już znajduje sie w tej bazie.")
                    time.sleep(2)
                
                else:
                    where = words_segreagtor.Segregator(self.lessons_language, self.pl_words[self.last_word], self.alien_words[self.last_word])
                    where.AddToHardWordsLists()
                    print("Słówko zostało dodane do listy 'Trudnych'")
                    time.sleep(2)

            # add word to "I know these words list"
            elif choice == '2':
                self.DownloadKnow_HardWordsLists("know_words")
                if self.alien_words[self.last_word] in self.segregator_words:
                    print("Słówko już znajduje sie w tej bazie.")
                    time.sleep(2)
                
                else:
                    where = words_segreagtor.Segregator(self.lessons_language, self.pl_words[self.last_word], self.alien_words[self.last_word])
                    where.AddToKnowWordsLists()
                    print("Słówko zostało dodane do listy 'Znanych'")
                    time.sleep(2)

            elif choice == '3':
                break
            
            else:
                continue
            
            # change word index
            self.last_word += 1

            if self.last_word == self.words_quantity:
                self.last_word = 0
