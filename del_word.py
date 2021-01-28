# import modules
import learn, time

class DelWord:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = []
        self.alien_words = []
        self.word_to_delete = "word"
        lists = learn.Learn(self.lessons_language)
        lists.DownloadWordsLists(self)

    def Delete(self):
        print(self.alien_words)
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