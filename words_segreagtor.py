class Segregator:
    def __init__(self, lessons_language, pl_word, alien_word):
        self.lessons_language = lessons_language
        self.pl_word = pl_word
        self.alien_word = alien_word
    
    def AddToKnowWordsLists(self):
        with open(str(self.lessons_language) + "/" + "know_words.txt", "a+", encoding='utf8') as file:
            file.write(self.alien_word + "\n")
            file.write(self.pl_word + "\n")
    
    def AddToHardWordsLists(self):
        with open(str(self.lessons_language) + "/" + "hard_words.txt", "a+", encoding='utf8') as file:
            file.write(self.alien_word + "\n")
            file.write(self.pl_word + "\n")
    
    def Print(self):
        print(self.pl_words)
        print(self.alien_words)