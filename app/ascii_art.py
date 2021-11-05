from time import sleep
from app.clear_function import clear_terminal


# ASCII Art from https://patorjk.com/software/taag/#p=display&f=Puffy&t=Welcome
# and adjusted to fit
def hangman_ascii_welcome():
    '''
    Prints the Welcome message to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""


                 _       _          _
                ( )  _  ( )        ( )
                | | ( ) | |   __   | |    ___    _     ___ ___     __
                | | | | | | / __ \\ | |  / ___) / _ \\ /  _   _  \\ / __ \\
                | (_/ \\_) |(  ___/ | | ( (___ ( (_) )| ( ) ( ) |(  ___/
                 \\___x___/  \\____)(___) \\____) \\___/ (_) (_) (_) \\____)



    """)
    print("*" * 80)
    sleep(.5)

    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""


                                 _____
                                (_   _)
                                  | |   _
                                  | | / _ \\
                                  | |( (_) )
                                  (_) \\___/


    """)
    print("*" * 80)
    sleep(.5)

    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""

                 _   _
                ( ) ( )
                | |_| |   _ _   ___     __    ___ ___     _ _   ___
                |  _  | / _  )/  _  \\ / _  \\/  _   _  \\ / _  )/  _  \\
                | | | |( (_| || ( ) |( (_) || ( ) ( ) |( (_| || ( ) |
                (_) (_) \\__,_)(_) (_) \\__  |(_) (_) (_) \\__,_)(_) (_)
                                     ( )_) |
                                      \\____/

    """)
    print("*" * 80)
    sleep(.5)


def hangman_ascii_lets_play():
    '''
    Prints the words Let's Play to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""

             _             _    _           ___   _
            ( )           ( )_ ( )         (  _ \\(  )
            | |       __  |  _)\\/   ___    | |_) )| |    _ _  _   _
            | |  _  / __ \\| |     / ,__)   | ,__/ | |  / _  )( ) ( )
            | |_( )(  ___/| |_    \\__, \\   | |    | | ( (_| || (_) |
            (____/  \\____) \\__)   (____/   (_)   (___) \\__,_) \\__, |
                                                             ( )_| |
                                                              \\____/

    """)
    print("*" * 80)
    sleep(.5)


def hangman_ascii_hangman():
    '''
    Prints the word hangman to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""

                 _   _
                ( ) ( )
                | |_| |   _ _   ___     __    ___ ___     _ _   ___
                |  _  | / _  )/  _  \\ / _  \\/  _   _  \\ / _  )/  _  \\
                | | | |( (_| || ( ) |( (_) || ( ) ( ) |( (_| || ( ) |
                (_) (_) \\__,_)(_) (_) \\__  |(_) (_) (_) \\__,_)(_) (_)
                                     ( )_) |
                                      \\____/

    """)
    print("*" * 80)
    sleep(.5)


def hangman_ascii_bye():
    '''
    Prints the Bye message to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""


       _____  _                    _                 ___
      (_   _)( )                  ( ) _            / ___)
        | |  | |__     _ _   ___  | |/ )   ___    | (__   _    _ __
        | |  |  _  \\ / _  ) / _  \\| , <  / ,__)   | ,__)/ _ \\ (  __)
        | |  | | | |( (_| || ( ) || |\\`\\ \\__, \\   | |  ( (_) )| |
        (_)  (_) (_) \\__,_)(_) (_)(_)(__)(____/   (_)   \\___/ (_)




    """)
    print("*" * 80)
    sleep(.5)

    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""


                 ___    _
                (  _ \\ ( )                _
                | |_) )| |    _ _  _   _ (_)  ___     __
                |  __/ | |  / _  )( ) ( )| |/  _  \\ / _  \\
                | |    | | ( (_| || (_) || || ( ) |( (_) |
                (_)   (___) \\__,_) \\__, |(_)(_) (_) \\__  |
                                  ( )_| |          ( )_) |
                                  \\____/           \\____/


    """)
    print("*" * 80)
    sleep(.5)

    clear_terminal()
    print('\n' * 4)
    print("*" * 80)
    print("""


                             ___    _     _  ___
                            (  _ \\ ( )   ( )(  _ \\
                            | (_) ) \\ \\_/ / | (_(_)
                            |  _ <    \\ /   |  _)_
                            | (_) )   | |   | (_( )
                            (____/    (_)   (____/



    """)
    print("*" * 80)
    sleep(.5)
    clear_terminal()


def hangman_ascii_high_scores():
    '''
    Prints the words High Score to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n')
    print("""
         _   _            _         ___
        ( ) ( ) _        ( )       (  _ \\
        | |_| |(_)   __  | |__     | (_(_)   ___    _    _ __   __   ___
        |  _  || | / _  \\|  _  \\    \\__ \\  / ___) / _ \\ (  __)/ __ \\/  _)
        | | | || |( (_) || | | |   ( )_) |( (___ ( (_) )| |  (  ___/\\__  \\
        (_) (_)(_) \\__  |(_) (_)    \\____) \\____) \\___/ (_)   \\____)(____/
                  ( )_) |
                   \\____/
    """)


def hangman_ascii_congratulations():
    '''
    Prints the word congratulations message to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n')
    print("*" * 80)
    print("""
             _       _         _    _       ___
            ( )  _  ( )       (_ ) (_ )    (  _ \\
            | | ( ) | |   __   | |  | |    | | ) |    __   ___     __
            | | | | | | / __ \\ | |  | |    | | | ) / _  \\/  _  \\ / __ \\
            | (_/ \\_) |(  ___/ | |  | |    | |_) |( (_) )| ( ) |(  ___/
             \\___x___/  \\____)(___)(___)   (____/  \\___/ (_) (_) \\____)
            _     _                ___                              _
           ( )   ( )              (  _ \\                           ( )
            \\ \\_/ / __    _   _   | (_(_)    _ _  _   _    __     _| |
             \\   / / _ \\ ( ) ( )   \\__  \\  / _  )( ) ( ) / __ \\ / _  |
              | | ( (_) )| (_) |   ( )_) |( (_| || \\_/ |(  ___/( (_| |
              (_)  \\___/  \\___/     \\____) \\__,_) \\___/  \\____) \\__,_)
                             _____  _
                            (_   _)( )
                              | |  | |__     __    ___ ___
                              | |  |  _  \\ / __ \\/  _   _  \\
                              | |  | | | |(  ___/| ( ) ( ) |
                              (_)  (_) (_) \\____)(_) (_) (_)
    """)
    print("*" * 80)
    sleep(1)
    clear_terminal()


def hangman_ascii_die():
    '''
    Prints the sorry message to the screen in ASCII ART
    '''
    clear_terminal()
    print('\n')
    print("""                 ___                             _     _
                (  _ \\                          ( )   ( )
                | (_(_)  _   _ __ _ __ _   _     \\ \\_/ /_   _   _
                 \\__ \\ / _ \\(  __(  __( ) ( )      \\ // _ \\( ) ( )
                ( )_) ( (_) | |  | |  | (_) |      | ( (_) | (_) |
                 \\____ \\___/(_)  (_)   \\__, |      (_ \\___/ \\___/
                                      ( )_| |
                                       \\___/
                         ___                _      _        _  _
                        (  _ \\             ( )    ( )      ( )( )_
                        | ( (_)  _   _   _ | |   _| | ___  |/ | ,_)
                        | |  _ / _ \\( ) ( )| | / _  /  _  \\   | |
                        | (_( ( (_) | (_) || |( (_| | ( ) |   | |_
                        (____/ \\___/ \\___/ (_) \\__,_(_| |_)    \\__)
                 ___                          ___  _
                (  _ \\                      (_   _( )
                | (_(_)  _ _ _   _   __       | | | |__    __   ___ ___
                 \\__ \\ / _  ( ) ( )/ __ \\     | | |  _  \\/ __\\/  _   _  \\
                ( )_) ( (_| | \\_/ (  ___/     | | | | | (  ___| ( ) ( ) |
                 \\___/ \\__,_|\\___/ \\____)     (_) (_) (_|\\____(_) (_) (_)
    """)
    sleep(1)
    clear_terminal()
