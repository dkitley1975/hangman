def display_hangman(tries):
    """
    Images to represent the different stages in the hanging Hangman images
    initially source from a youtube tutorial added additional stages
    and amended the graphics to my reguirements.
    """

    stages = [
        # final state: hunghead, torso, both arms, and both legs
        """
                                    --------
                                    |      |
                                    |     [x]
                                    |     \\|/
                                    |      |
                                    |     / \\
                                    --------
        """,
        # head, torso, both arms, and both legs
        """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|/
                                    |      |
                                    |     / \\
                                    --------
        """,
        # head, torso, both arms, and one leg
        """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|/
                                    |      |
                                    |     /
                                    --------
        """,
        # head, torso, and both arms
        """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|/
                                    |      |
                                    |
                                    --------
        """,
        # head, torso, and one arm
        """
                                    --------
                                    |      |
                                    |      O
                                    |     \\|
                                    |      |
                                    |
                                    --------
        """,
        # head and torso
        """
                                    --------
                                    |      |
                                    |      O
                                    |      |
                                    |      |
                                    |
                                    --------
        """,
        # head
        """
                                    --------
                                    |      |
                                    |      O
                                    |
                                    |
                                    |
                                    --------
        """,
        # initial empty state, with man beside
        """
                                    --------
                                    |      |
                                    |
                                    |
                                    |
                                    |
                                    --------
        """,
        # initial empty state
        """
                                    --------
                                    |
                                    |
                                    |
                                    |
                                    |
                                    --------
        """,
    ]
    return stages[tries]
