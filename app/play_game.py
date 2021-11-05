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
    nl_1 = '\n'
    nl_2 = '\n' * 2
    nl_5 = '\n' * 5
    word_completion = "_" * len(word)
    total_letters = len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    clear_terminal()
    print(f"{nl_5}{'Hello and welcome to my Hangman Game':^80}{nl_1}")
    player_name = input(' ' * 32 + "Enter your name: \n" + ' ' * 38).title()
    clear_terminal()
    print('\n' * 2)
    print(f"{'Hello ' + player_name + ' lets play Hangman!':^80}{nl_1}")
    print('{:^80}'.format("there are " + str(total_letters) +
                          " letters in the word") + nl_1)
    print(display_hangman(tries) + nl_1)
    print(f"{word_completion:^80}{nl_1}")
    while not guessed and tries > 0:
        guess = input(' ' * 23 + "Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('{:^80}'.format("You have already guessed " + guess +
                                      " please try another letter"))
                sleep(1)
            elif guess not in word:
                print('{:^80}'.format("Sorry " + guess + " is not in the word"
                                      " please try another letter"))
                sleep(1)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"{'Congratulations ' + guess + ' is in the word.':^80}")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in
                           enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('{:^80}'.format("You have already guessed " + guess +
                                      " please try another letter"))
                sleep(1)
            elif guess != word:
                print('{:^80}'.format("Sorry " + guess +
                                      " is not the word please try again"))
                sleep(1)
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        clear_terminal()
        guessed_letters_string = ", ".join(guessed_letters)
        print(f"{'Your previously guesses letters are:':^80}")
        print(f"{guessed_letters_string :^80}")
        print(display_hangman(tries))
        print(f'{word_completion:^80}')
        print('{:^80}'.format("there are " + str(total_letters) +
                              " letters in the word") + nl_1)
    if guessed:
        new_score = []
        new_score.extend((tries, player_name, word.title()))
        update_highscores(new_score)
        hangman_ascii_congratulations()
        print('\n' * 9)
        print(f"{'Congratulations ' + player_name + '.':^80}" + nl_1)
        print(f"{'You guessed the word ' + word + ', correctly.':^80}" + nl_1)
    else:
        hangman_ascii_die()
        print('\n' * 9)
        print(f"{player_name + ', you ran out of tries.':^80}" + nl_1)
        print(f"{'The word was ' + word + '.':^80}" + nl_1)
