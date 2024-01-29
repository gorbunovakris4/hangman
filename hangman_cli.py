"""
module providing console user interface for hangman game
"""
from hangman import HangmanGame

class ConsoleUI:
    """
    class  providing console user interface for hangman game
    """
    def __init__(self, max_mistakes:int = 5):
        self.game = HangmanGame(max_mistakes)
        self.is_over = False

    @staticmethod
    def start():
        """
        print starting string
        """
        print("Let's start!")

    def guess(self) -> bool:
        """
        ask user to guess a letter.
        :return: boolean value. True if guess is approved. False if entered string was not letter or
                                letter is a duplicate of one of the previous guesses
        """
        print(f'The word: {self.game.show_word()}')
        print("Guess a letter:")
        letter = input()
        if not letter.isalpha():
            print("Enter the letter from English alphabet, please")
            return False
        if len(letter) != 1:
            print("Letter must be single-character string. Try again")
            return False
        letter = letter.lower()
        is_guessed, is_repeated, is_over = self.game.check_letter(letter)
        if is_over:
            print("Game comes to an end.")
            if self.game.is_lost():
                print('You lost!')
            else:
                print('You won!')
            self.is_over = True
            return True

        if is_repeated:
            if is_guessed:
                print("Right, but you have already opened this letter. Try again:")
            else:
                print("Missed, but you have already tried this letter. Try again:")
            return False

        if is_guessed:
            print("Hit!")
        else:
            print(f"Missed, mistake {self.game.mistakes_cnt()} out of {self.game.max_mistakes}")
        return True

    def restart(self, max_mistakes:int = 5):
        """
        :param max_mistakes: optional, max amount of mistakes
        """
        self.game = HangmanGame(max_mistakes)
        self.is_over = False

    def ask_for_restart(self):
        """
        asks user if  he wants to restart the game
        """
        if not self.is_over:
            raise ValueError("game is in progress")
        print("Do you want to restart the game?\n Print 'yes' without quotes to restart:")
        if (_ := input()) == 'yes':
            self.restart()

    def full_game(self):
        """
        main function to run the app
        """
        self.start()
        while not self.is_over:
            while not self.is_over:
                move_is_done = False
                while not move_is_done:
                    move_is_done = self.guess()
            self.ask_for_restart()
