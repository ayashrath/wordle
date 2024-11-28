#! /bin/python3

import typer
from wordle_implementation import Wordle

wordle_instance = Wordle()

typer.run(wordle_instance.play_interactive)
