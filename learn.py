# import modules
import os, time
import words_segreagtor

class Learn:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = "pl"
        self.alien_words = "alien"
        self.last_word = 0
        self.words_quantity = 0
        self.segregator_words = []
    
    def DownloadWordsListsToRepeat(self, lvl):
        alien_words = []
        pl_words = []
        all_words = []

        # download alien words
        with open(str(self.lessons_language) + "/" + str(lvl) + ".txt", "r+", encoding='utf8') as file:
            lines = file.read().split("\n")
            for line in lines:
                if len(line) > 0:
                    all_words.append(line)
                else:
                        continue

        for word in all_words:
            word_index = all_words.index(word)
            if word_index % 2 == 0:
                alien_words.append(word)
            elif word_index % 2 == 1:
                pl_words.append(word)

        self.alien_words = alien_words
        self.pl_words = pl_words
    
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
    
    def DownloadKnow_HardWordsLists(self, lista):
        # download actual know words list
            lis = []
            with open(str(self.lessons_language) + "/" + str(lista) + ".txt", "r", encoding='utf8') as file:
                lines = file.read().split("\n")
                for line in lines:
                    if len(line) > 0:
                        lis.append(line)
                    else:
                        continue
            self.segregator_words = lis

    def StartLearn(self, learn_type):
        if learn_type == "all":
            self.DownloadWordsLists()
        elif learn_type == "hard_words":
            self.DownloadWordsListsToRepeat(learn_type)
        elif learn_type == "know_words":
            self.DownloadWordsListsToRepeat(learn_type)

        self.words_quantity = len(self.alien_words)

        while True:
            try:
                if self.words_quantity == 0:
                    print("Lista nie posiada jeszcze żadnych słówek.")
                    time.sleep(3)
                    break

                os.system('cls')
                print(self.alien_words[self.last_word], "\t\t\tAktualnie w bazie znajduse się", str(len(self.pl_words)), "słówek.\n")
                input("Sprawdź --> Enter")
                os.system('cls')
                print(self.alien_words[self.last_word], " <-> ", self.pl_words[self.last_word], "\t\t\tAktualnie w bazie znajduse się", str(len(self.pl_words)), "słówek.\n")
                choice = input("\nDalej --> Enter\nDodaj do 'Trudne' --> '1' + Enter\nDodaj do 'Zapamiętane' --> '2' + Enter\nPrzerwij naukę --> '3' + Enter\n-->  ")

                # add word to "Hard words list"
                if choice == '1':
                    self.DownloadKnow_HardWordsLists("hard_words")
                    if self.alien_words[self.last_word] in self.segregator_words:
                        print("Słówko już znajduje sie w tej bazie.")
                        time.sleep(2)
                        # change word index
                        self.last_word += 1
                        if self.last_word == self.words_quantity:
                            self.last_word = 0
                    
                    else:
                        where = words_segreagtor.Segregator(self.lessons_language, self.pl_words[self.last_word], self.alien_words[self.last_word])
                        where.AddToHardWordsLists()
                        print("Słówko zostało dodane do listy 'Trudnych'")
                        time.sleep(2)
                        # change word index
                        self.last_word += 1
                        if self.last_word == self.words_quantity:
                            self.last_word = 0

                # add word to "I know these words list"
                elif choice == '2':
                    self.DownloadKnow_HardWordsLists("know_words")
                    if self.alien_words[self.last_word] in self.segregator_words:
                        print("Słówko już znajduje sie w tej bazie.")
                        time.sleep(2)
                        # change word index
                        self.last_word += 1
                        if self.last_word == self.words_quantity:
                            self.last_word = 0
                    
                    else:
                        where = words_segreagtor.Segregator(self.lessons_language, self.pl_words[self.last_word], self.alien_words[self.last_word])
                        where.AddToKnowWordsLists()
                        print("Słówko zostało dodane do listy 'Znanych'")
                        time.sleep(2)
                        # change word index
                        self.last_word += 1
                        if self.last_word == self.words_quantity:
                            self.last_word = 0

                elif choice == '3':
                    break
                
                else:
                    # change word index
                    self.last_word += 1
                    if self.last_word == self.words_quantity:
                        self.last_word = 0
                    continue
            
            except IndexError:
                self.last_word = 0
                continue
