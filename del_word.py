# import modules
import learn, time

class DelWord:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = []
        self.alien_words = []
        self.word_to_delete = "word"
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

    def Delete(self):
        print(("Jakie słówko chcesz usunąć?"))
        self.word_to_delete = input("Wprowadź słówko w języku polskim: ")
        if self.word_to_delete in self.pl_words:
            word_index = self.pl_words.index(self.word_to_delete)
            del self.pl_words[word_index]
            del self.alien_words[word_index]

            # delete word from alien words list
            with open(str(self.lessons_language) + "/" + "alien-words.txt", "w", encoding='utf8') as file:
                for word in self.alien_words:
                    file.write(word + "\n")

            # delete word from polish words list
            with open(str(self.lessons_language) + "/" + "pl-words.txt", "w", encoding='utf8') as file:
                for word in self.pl_words:
                    file.write(word + "\n")

            print("Słówko zostało poprawnie usięte.")
            time.sleep(3)

        else:
            print("Nie znaleziono słówka, sprawdź poprawność pisowni.")
            time.sleep(3)