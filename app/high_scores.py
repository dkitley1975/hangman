import gspread
from google.oauth2.service_account import Credentials
from app.clear_function import clear_terminal
from app.ascii_art import hangman_ascii_high_scores

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangmanhighscores')

High_Scores = SHEET.worksheet('scores')
Scores = High_Scores.get_all_values()
Update_Score = SHEET.worksheet("scores")
Reorder_Sheet = SHEET.worksheet("scores")
Delete_Rows = SHEET.worksheet("scores")


def display_highscores():
    """
    clears the terminal and displays the highscores
    from the spreadsheet.
    """
    clear_terminal()
    hangman_ascii_high_scores()
    print('\n')
    for Score,Name,Word in Scores[:10]:
        print (f'{ Score: ^30}{ Name: ^20}{ Word: ^30}')

    print('\n')
    input(' ' * 23 + "Press Enter to return to the menu \n"+ ' ' * 40)
    clear_terminal()


def update_highscores(new_score):
    """
    updates the highscores to the spreadsheet.
    """
    Update_Score.append_row(new_score)
    Reorder_Sheet.sort((2, 'des'))
    Delete_Rows.delete_rows(10, 11)
