import requests


def get_word():
    """
    requests a single random word form the hangman.api
    and converts it to uppercase before returning the word
    """
    url = "https://random-word-api.herokuapp.com/word?number=1"

    response = requests.request("GET", url)
    answer = response.json()
    return answer[0].upper()
