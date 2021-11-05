import sys

from app.clear_function import clear_terminal
from app.ascii_art import hangman_ascii_welcome
from app.ascii_art import hangman_ascii_bye
from app.ascii_art import hangman_ascii_lets_play
from app.ascii_art import hangman_ascii_hangman
from app.get_new_word import get_word
from app.play_game import play
from app.high_scores import display_highscores
from app.rules import display_rules

def welcome():
    """
    Displays the welcome message.
    """
    hangman_ascii_welcome()

def menu():
    """
    Displays the navigation to start a game, view high scores, view rules or quit.
    """
    clear_terminal()
    print('\n' * 3)
    print(f"{'  Main Menu ! ':*^80}")
    print('\n' * 2)
    print(f"{' 1: Play Hangman ':^80}")
    print('\n' * 1)
    print(f"{' 2: View High Scores ':^80}")
    print('\n' * 1)
    print(f"{' 3: Rules ':^80}")
    print('\n' * 1)
    print(f"{' 4: QUIT ':^80}")
    print('\n' * 2)
    while True:
        player_menu_selection = input(" " * 21 +
         " Please make a choice (1, 2, 3 or 4): \n" + ' ' * 39)
        if player_menu_selection == '1':
            hangman_ascii_lets_play()
            hangman_ascii_hangman()
            word = get_word()
            play(word)
            while input(' ' * 20 +
             "Would you like to play again? (Y/N) \n" + ' ' * 39).upper() == "Y":
                word = get_word()
                play(word)
                clear_terminal()
            menu()
        elif player_menu_selection == '2':
            display_highscores()
            menu()
        elif player_menu_selection == '3':
            display_rules()
            menu()
        elif player_menu_selection == '4':
            hangman_ascii_bye()
            sys.exit()
        else:
            print(f"{' Must choose 1, 2, 3 or 4 ! ':^80}")

welcome()
menu()
