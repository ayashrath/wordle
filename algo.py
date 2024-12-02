"""
This file implements the algorithm to solve the puzzle
"""
import pandas as pd
from typing import Dict
from wordle_implementation import Wordle

"""
- A Tuple that contains 2 parts
                - The first tells the status of the game
                    - 0: Game is still on
                    - 1: You won
                    - 2: You lost
                    - -1: Input invalid
                    - -2: Attempts filled, but not lost
                    - -3: Repeat input
                - A dict that contains both the index match chars along with only the match chars
                    - For example {"ind_match":[1], "belong_match": [3, 4]}
                    - At index 1 char from both string match, while at index 2 and 4 the char in input belong to choosen
                    - the ind are 0 - 4, just to make life easier if there is any repeating char that matches
                    - {} if the first is an error
                    - if lost {"<win_word>":<attempt_lst>} is the dict
                    - if won {"<win_word>":<attempt_lst>} is the dict
"""

PATH_ANS_WEIGHT = "nyt-word-score-ans-list-ans-weighted.csv"
PATH_GUESS_WEIGHT = "nyt-word-score-guess-list-ans-weighted.csv"
START_WORD = "irate"  # refer to the wordle-inverstigation notebook if you want to know why


def solve_wordle_instance(instance: Wordle) -> Dict:
    """
    Solving algorithm

    Parameters:
        - instance: The wordle game object

    Return:
        - {
            won: bool, {true if won}
            choosen_word: str,
            steps: int,
            all_choosen_words: tup {no null}
        }

    Errors:
        - Runtime error
            - -1 = Input invalid
            - -2 = No more steps allowed
            - -3 = It tried to input the same value

    """

    for i in range(6):
        if i == 0:
            state, match_dict = instance.play_machine(START_WORD)
            if state < 0:
                raise RuntimeError("Error Code: {}".format(str(state)))
            continue
        
        pass  ## actual content
