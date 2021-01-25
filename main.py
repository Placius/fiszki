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
                        if choice == 1:
                            self.lesson = learn.Learn(self.actual_lessons_language)
                            self.lesson.StartLearn()

                        elif choice == 2:
                            pass

                        elif choice == 3:
                            pass

                        elif choice == 4:
                            pass

                        elif choice == 5:
                            pass

                        elif choice == 6:
                            pass

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