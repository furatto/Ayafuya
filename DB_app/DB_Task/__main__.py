import os

from .src import First


def start_menu():
    os.system('clear')
    print("ハック用データベース\n1:始める 2:やめる")
    x = input()
    if x != "1" and x != "2":
        print("write again\n")
        os.system('PAUSE')
        return start_menu()
    return First(x)


start_menu()
