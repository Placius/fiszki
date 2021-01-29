import random, os, time

class Test:
    def __init__(self, lessons_language):
        self.lessons_language = lessons_language
        self.pl_words = []
        self.alien_words = []

        self.points = 0
        self.max_points = 15
        self.test_list_alien = []
        self.test_list_pl = []

        self.DownloadWordsLists()
        self.ChooseWordsToTest()
    
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
    
    def ChooseWordsToTest(self):
        random_index = []
        length = int(len(self.pl_words)-1)
       
        self.test_list_alien.append("empty")
        self.test_list_pl.append("pusty")

        if len(self.pl_words) < 15:
            l = len(self.pl_words)
            self.max_points = l-1
            self.test_list_alien = self.alien_words
            self.test_list_pl = self.pl_words

        else:
            l = 15

            for i in range(0, l):

                while True:
                    index = random.randint(0,length)
                    if index in random_index:
                        continue
                    else:
                        random_index.append(index)
                        break

            for index in random_index:
                self.test_list_alien.append(self.alien_words[index])
                self.test_list_pl.append(self.pl_words[index])
    
    def StartTest(self):
        try:
            for i in range(0, len(self.test_list_alien)-1):
                os.system("cls")
                print("Pytanie nr.", i+1)
                print(self.test_list_alien[i])
                try_this = input("Odpowiedź: ")
                if try_this.lower() == self.test_list_pl[i].lower():
                    os.system("cls")
                    print(self.test_list_alien[i], " <-----> ", self.test_list_pl[i])
                    print("Poprawnie!")
                    time.sleep(2)
                    self.points += 1
                
                else:
                    os.system("cls")
                    print(self.test_list_alien[i], " <-----> ", self.test_list_pl[i])
                    print("Niepoprawnie!")
                    time.sleep(2)
            os.system("cls")
            print("Udało Ci się uzyskać", str(self.points) + "/" + str(self.max_points) + "pkt.")

            time.sleep(4)
        
        except IndexError:
            print("W bazie znajduje się póki co zbyt mała liczba słówek!")
            time.sleep(4)