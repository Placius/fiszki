# Createt by Krystian Płatek
# 25.01.2021

# git remote add origin https://github.com/Placius/fiszki.git
# git branch -M main     
# git push -u origin main

# import standard modules
import sys

# import my modules
import menu
import learn
import add_word
import del_word

# general class

class Main:
    def __init__(self):
        self.general_menu = menu.GeneralMenu()
        self.second_menu = menu.ChooseLanguageMenu()
        self.third_menu = menu.InsideLanguageMenu()
        self.actual_lessons_language = "polish"
        self.lesson = "lesson"
    
    def Begin(self):
        while True:
            self.general_menu.ShowMenu()
            choice = self.general_menu.Choices()
            if choice == 1:
                while True:
                    self.second_menu.ShowMenu()
                    choice = self.second_menu.Choices()
                    if choice == 1:
                        self.actual_lessons_language = "english"

                    elif choice == 2:
                        self.actual_lessons_language = "deutsch"

                    elif choice == 3:
                        break

                    else:
                        self.second_menu.Quit()
                    
                    if choice == 1 or choice == 2:
                        self.third_menu.ShowMenu()
                        choice = self.third_menu.Choices()
                        self.lesson = learn.Learn(self.actual_lessons_language)
                        # all words
                        if choice == 1:
                            self.lesson.StartLearn("all")

                        # hard words
                        elif choice == 2:
                            self.lesson.StartLearn("hard_words")

                        # I know thats words learn and repeat
                        elif choice == 3:
                            self.lesson.StartLearn("know_words")
                        
                        # test
                        elif choice == 4:
                            pass
                        
                        # add new word
                        elif choice == 5:
                            new_word = add_word.NewWord(self.actual_lessons_language)
                            new_word.AddWord()

                        # del word
                        elif choice == 6:
                            delete_word = del_word.DelWord(self.actual_lessons_language)
                            delete_word.Delete()

                        # back to menu
                        elif choice == 7:
                            break

                        else:
                            self.third_menu.Quit()

            # change language of menus
            elif choice == 2:
                pass

            else:
                self.general_menu.Quit()



# Run App

main = Main()

main.Begin()