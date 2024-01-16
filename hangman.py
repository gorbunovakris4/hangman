"""
module providing class HangmanGame with game logic
"""

import random


class HangmanGame:
    """
    Class realizing logic of game Hangman
    """
    __words = ["hello", "world", "python", "object", "program", "string", "float", "abstract",
               "pattern", "decorator"]
    _word_cnt = 10

    @staticmethod
    def gen_word() -> str:
        """
        randomly generates index of word from pre-saved dictionary
        :return word: word to guess.
        """
        return HangmanGame.__words[random.randint(0, HangmanGame._word_cnt - 1)]

    def __init__(self, max_mistakes: int = 5):
        self.word = HangmanGame.gen_word()
        self.show = [0] * len(self.word)
        self.suggestions = set()
        self.mistakes = 0
        self.max_mistakes = max_mistakes
        self.left = len(self.word)

    def _reset_word(self, word: str):
        """
        set new word to guess. Does nothing if the new word is equal to the previous one
        :param: word: new word to be guessed.
        """
        if self.word == word:
            return
        self.word = word
        self.show = [0] * len(self.word)
        self.suggestions = set()
        self.mistakes = 0
        self.left = len(self.word)

    def is_over(self) -> bool:
        """
        :return: True if game is over. User won or lost the game
        """
        return self.is_lost() or self.is_won()

    def is_lost(self) -> bool:
        """
        :return: True if the game is lost by the user, False otherwise
        """
        return self.mistakes == self.max_mistakes

    def is_won(self) -> bool:
        """
        :return: True if the game is won by the user, False otherwise
        """
        return self.left == 0

    def check_letter(self, letter: str) -> tuple:
        """
        checks if the letter is not in word  or is already guessed
        :param letter: single-character string, where character is lowercase latin letter. Otherwise, Exception is raised
        :returns: tuple of two bool values.
            is_guessed: True, if the word contains letter
            is_repeated: True if the letter has already been tried
            is_over: True if the game is over. 5 mistakes were done.
        :raises:
        :raise ValueError: if the game is over or argument is invalid
        """
        if self.is_over():
            raise ValueError("the game is over")
        if len(letter) != 1 or not letter.isalpha() or not letter.islower():
            raise ValueError("letter must be single-character string, "
                             "where character is lowercase latin letter")
        is_repeated = letter in self.suggestions
        self.suggestions.add(letter)
        if letter not in self.word:
            if not is_repeated:
                self.mistakes += 1
            return False, is_repeated, self.is_over()
        if is_repeated:
            return True, True, self.mistakes == self.max_mistakes
        for pos in [i for i, let in enumerate(self.word) if let == letter]:
            self.show[pos] = 1
            self.left -= 1
        return True, False, self.is_over()

    def show_word(self) -> str:
        """
        :returns: string, representing non-guessed letters as *
        """
        return ''.join([let if self.show[i] else '*' for i, let in enumerate(self.word)])

    def mistakes_cnt(self) -> int:
        """
        :return: amount of done mistakes
        """
        return self.mistakes
