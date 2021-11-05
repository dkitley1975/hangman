from app.clear_function import clear_terminal


def display_rules():
    '''
    Prints the Rules for Hangman
    '''
    # ASCII Art from:
    # https://patorjk.com/software/taag/#p=display&f=Puffy&t=Welcome
    # and adjusted to fit
    clear_terminal()
    print("*" * 80)
    print("""             _  _                                  ___       _
            | || |__ _ _ _  __ _ _ __  __ _ _ _   | _ \\_   _| |___ ___
            | __ / _` | ' \\/ _` | '  \\/ _` | ' \\  |   / |_| | / -_|_-<
            |_||_\\__,_|_||_\\__, |_|_|_\\__,_|_||_| |_|__\\____|_\\___/__/
                            |___/

    HOW TO PLAY: The executioner will retrieve a word, and will draw an empty
    Gallows. The executioner will draw an underscore for each letter.
    The player will guess a letter. If that letter is in the word then the
    letter will replace the underscore everywhere it would appear and display
    the players guesses. If the letter isn't in the word then a body part will
    be added to the gallows (noose, head, body, left arm, right arm, left leg,
    right leg). The player will continue guessing letters until they can either
    solve the word or all the parts are on the gallows.

    TO WIN: The executioner wins if the full body is hanging from the gallows.
    The player wins if they guess the word before the person is hung.""")
    print("*" * 80)
    print('\n')
    input(" " * 24 + "Press Enter to return to the menu \n" + ' ' * 39)
    clear_terminal()
