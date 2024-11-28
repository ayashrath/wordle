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
            self.word_list = [line.strip() for line in fh.readlines()]
            self.choosen_word = random.choice(self.word_list)
            self.attempts = (None, None, None, None, None, None)  # as a game allows 6 attempts

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
        temp = list(self.attempts)
        temp[ind] = val

        self.attempts = tuple(temp)

    def __get_word_list(self):
        """
        Returns:
            - The word list that forms the knowledge base for the program
        """
        return self.word_list

    def __update_game_attempts(self, inp: str) -> int:
        """
        Update attempt list where the 1st None exists and also check for uniqueness

        Parameter:
            - inp: The input

        Returns:
            - 0: No problems
            - -1: Uniqueness Issue
        """

        if inp in self.__get_attempts():
            return -1

        current_attempts = self.__get_attempts()
        self.__update_attempts(current_attempts.index(None), inp)

        return 0

    def __check_input_validity(self, inp: str) -> int:
        """
        Checks if the input is valid or not.
        The test is basically check if it is a 5 len str, if it is uses english alphabets
        and finally if it is even actually a english word

        Parameters:
            - inp: The input

        Returns:
            - 1: The length is incorrect
            - 2: The word doesn't use english alphabets
            - 4: If the word doesn't belong in the knowledgebase
            - Sum of above int, if a mix of these (in base 2, shows the features that were selected)
        """
        result = 0
        if len(inp) != 5:
            result += 1
        if not inp.isalpha():
            result += 2
        if inp not in self.__get_word_list():
            result += 4

        return result

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

    def __check_letter_match_inp(self, inp: str) -> Dict[str, List[int]]:
        """
        Checks the letters from input that match with the output, along with if their indexes also match

        Parameter:
            - inp: The input

        Returns:
            - A dict that contains both the index match chars along with only the match chars
                - For example {"ind_match":[1], "belong_match": [3, 4]}
                - At index 1 char from both string match, while at index 2 and 4 the char in input belong to choosen
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
                    result["ind_match"].append(ind)
                else:
                    result["belong_match"].append(ind)

            ind += 1

        return result

    def __format_str(self, inp: str, exact_match_inds: List[int], belong_match_inds: List[int]) -> str:
        """
        Based on the match status, format the string

        If it is a match of char and indexes then caps
        if it is a belong match it is a bold

        Parameters:
            - inp: The input string
            - exact_match_inds: The list of indexes where exact match occur
            - belong_match_inds: The list of indexes where the belong matches occur

        Returns:
            - formated ascii string implementing it

        Limitations:
            - The terminal app must support the feature, else it is useless
        """

        bold_code = "\033[1m"
        reset_code = "\033[0m"

        formatted_str = ""

        counter = 0
        for char in inp:
            if counter in exact_match_inds:
                char = char.upper()
                formatted_str += char + " "
            elif counter in belong_match_inds:
                formatted_str += bold_code + char + reset_code + " "
            else:
                formatted_str += char + " "

            counter += 1

        return formatted_str

    def reset(self):
        """
        Reset the entire board, excluding the choosen word
        """
        for ind in range(6):
            self.__update_attempts(ind, None)

    def play_interactive(self) -> None:
        """
        The full game loop
        """

        if self.__get_attempts() != (None, None, None, None, None, None):
            print("Resetting!")
            self.reset()

        print("-----------------------------------------------------------------------------------------------\n\n")
        print("The word has been choosen! You have 6 attemps, and need to provide a valid 5-letter english word input")
        print("The program will provide you feedback based on char matches, and you need to guess the word exactly")
        print("Your Terminal App must support bold.")
        print("Caps = At that position the character from your input matches exactly with the choosen word")
        print("Bold = The characters in your input with these belong to choosen, but not at these positions")
        print("------------------------------------------------------------------------------------------------\n\n")

        while None in self.__get_attempts():
            inp = input("{} input: ".format(6 - self.__get_attempts().count(None) + 1)).lower()
            validity_score = self.__check_input_validity(inp)
            if validity_score != 0:
                validity_score_bin = bin(validity_score)[2:]  # remove 0b
                if validity_score_bin[0] == "1":
                    print("Not within the word knowledgebase, try again!")
                if validity_score_bin[1] == "1":
                    print("It doesn't use English Alphabets, try again!")
                if validity_score_bin[2] == "1":
                    print("Wrong Length, try again!")

                print("\n\n")
                continue

            if self.__check_word_match(inp):
                self.__update_game_attempts(inp)

                print("\n\nYou won!")
                print("The guesses you made are:", self.__get_attempts())
                break
            else:
                match_status = self.__check_letter_match_inp(inp)
                formatted_str = self.__format_str(inp, match_status["ind_match"], match_status["belong_match"])
                print(formatted_str)

                end_code = self.__update_game_attempts(inp)
                if end_code == -1:
                    print("It already has been inputed\n\n")  # no skip needed as count will not be effected

        else:
            print("\n\nYou lost :(")
            print("The guesses you made are:", self.__get_attempts())
            print("The word was: {}".format(self.__get_choosen_word()))

    def play_machine(self, inp: str) -> Tuple[int, Dict[str, List[int]]]:
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
                    - 2: You lost
                    - -1: Input invalid
                - A dict that contains both the index match chars along with only the match chars
                    - For example {"ind_match":[1], "belong_match": [3, 4]}
                    - At index 1 char from both string match, while at index 2 and 4 the char in input belong to choosen
                    - the ind are 0 - 4, just to make life easier if there is any repeating char that matches
        """
        pass
