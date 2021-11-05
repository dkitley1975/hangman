from time import sleep
from app.hangman_pics import display_hangman
from app.clear_function import clear_terminal
from app.high_scores import update_highscores
from app.ascii_art import hangman_ascii_die
from app.ascii_art import hangman_ascii_congratulations


def play(word):
    """
    Main game play function,
    """
    word_completion = "_" * len(word)
    total_letters = len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    clear_terminal()
    print('\n' * 5)
    print(f"{'Hello and welcome to my Hangman Game':^80}")
    print('\n' * 2)
    player_name = input(' ' * 25
     + "Please enter your name: \n" + ' ' * 35).title()
    clear_terminal()
    print('\n' * 2)
    print(f"{'Hello ' + player_name + ' lets play Hangman!':^80}")
    print('\n')
    print(display_hangman(tries))
    print('\n')
    print(f'{word_completion:^80}')
    print('\n')
    print(f"{'there are ' + str(total_letters) + ' letters in the word':^80}")
    print('\n' * 2)
    while not guessed and tries > 0:
        guess = input(' ' * 23 + "Please guess a letter or word: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{'You have already guessed ' + guess + ' please try another letter':^80}")
                sleep(1)
            elif guess not in word:
                print(f"{'Sorry, ' + guess + ', is not the word.':^80}")
                sleep(1)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"{'Congratulations ' + guess + ' is in the word.':^80}")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"{'You have already guessed ' + guess + ' please try another letter':^80}")
                sleep(1)
            elif guess != word:
                print(f"{'Sorry, ' + guess + ', is not the word.':^80}")
                sleep(1)
                sleep(1)
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        clear_terminal()
        print(word)
        guessed_letters_string = ",".join(guessed_letters)
        print('\n' * 4)
        print(f"{'Your previously guesses letters are:':^80}")
        print(f"{guessed_letters_string :^80}")
        print(display_hangman(tries))
        print(f'{word_completion:^80}')
        print(f"{'there are ' + str(total_letters) + ' letters in the word':^80}")
        print("\n")

    if guessed:
        new_score = []
        new_score.extend((tries, player_name, word.title()))
        update_highscores(new_score)
        hangman_ascii_congratulations()
        print(f"{'Congratulations ' + player_name + '.':^80}")
        print(f"{'You guessed the word ' + word + ', correctly.':^80}")
    else:
        hangman_ascii_die()
        print('\n' * 12)
        print(f"{player_name + ', you ran out of tries.':^80}")
        print(f"{'The word was ' + word + '.':^80}" "\n")
    