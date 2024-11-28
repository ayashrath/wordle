"""
Just a implementation of the game, to test with with the algo and also to run the algo
"""

import time
import random
from typing import List, Tuple, Dict


class Wordle:
    """
    It is the Wordle Game - Standard Rules

    Parameters:
        - path ("./valid-wordle-words.txt"): The path where the word list is at from which the word is choosen
        - seed (time.time()): If you want to use a seed, i.e., fix the choosen word using a fixed seed.

    Useage:
        - Use the "play_interactive" method to have a cli user experience
        - Use the "play_machine" method to run it by calls turn by turn from a program
    """

    def __init__(self, path: str = "./valid-wordle-words.txt", seed: int = time.time()):
        """
        Init
        """
        with open(path) as fh:
            random.seed = seed
            self.choosen_word = random.choice([line.strip() for line in fh.readlines()])
            self.attempts = (None, None, None, None, None, None)

    def __get_choosen_word(self) -> str:
        """
        Returns:
            - choosen word
        """
        return self.choosen_word

    def __get_attempts(self) -> Tuple[str, str, str, str, str, str]:
        """
        Returns:
            - attempts tuple
        """
        return self.attempts

    def __update_attempts(self, ind: int, val: str) -> None:
        """
        Updates the attempt tuple

        Parameters:
            - ind: The word turn
            - val: The input for the word turn supplied
        """
        self.attempts[ind] = val

    def __check_input_validity(self, inp: str) -> bool:
        """
        Checks if the input is valid or not

        Parameters:
            - inp: The input

        Returns:
            - True if they are the same, else False
        """
        if len(inp) != 5 or not inp.isalpha():
            return False
        return True

    def __check_word_match(self, inp: str) -> bool:
        """
        Checks if the input matches with the output or not

        Parameters:
            - inp: The input

        Returns:
            - True if the word matchs, else False
        """
        if inp == self.__get_choosen_word():
            return True
        return False

    def __check_letter_match_inp(self, inp: str) -> Dict[str, List[Tuple[int, str]]]:
        """
        Checks the letters from input that match with the output, along with if their indexes also match

        Parameter:
            - inp: The input

        Returns:
            - A dict that contains both the index match chars along with only the match chars
                - For example {"ind_match":[("a", 1)], "belong_match": [("c", 3), ("d", 4)]}
                - "a" matches with index too, "c", "d" only match, not index matches
                - "a" is at ind 1 in inp, "c: is at ind 3 in inp and "d" at ind 4 in inp
                - the ind are 0 - 4, just to make life easier if there is any repeating char that matches
        """

        choosen_word = self.__get_choosen_word()

        result = {
            "ind_match": [],
            "belong_match": [],
        }

        ind = 0
        for char in inp:
            if char in choosen_word:
                if char == choosen_word[ind]:
                    result["ind_match"].append((char, ind))
                else:
                    result["belong_match"].append((char, ind))

            ind += 1

        return result

    def play_interactive(self) -> None:
        """
        The full game loop
        """
        pass

    def play_machine(self, inp: str) -> Tuple[int, Dict[str, List[Tuple[int, str]]]]:
        """
        Allows playing a turn at a time, for a single game instance and returns data so
        a machine can see the state easily

        Parameters:
            - inp: The input word

        Return:
            - A Tuple that contains 2 parts
                - The first tells the status of the game
                    - 0: Game is still on
                    - 1: You won
                    - -1: You lost
                - A dict that contains both the index match chars along with only the match chars
                    - For example {"ind_match":[("a", 1)], "belong_match": [("c", 3), ("d", 4)]}
                    - "a" matches with index too, "c", "d" only match, not index matches
                    - "a" is at ind 1 in inp, "c: is at ind 3 in inp and "d" at ind 4 in inp
                    - the ind are 0 - 4, just to make life easier if there is any repeating char that matches
        """
        pass
