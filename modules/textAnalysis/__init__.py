import os

import pandas as pd

from Module import Module, Break, Continue
from modules.textAnalysis.Conversation import Conversation
from cli import EnumeratedChooseOption
from utils import filter_list_dir_by_extensions

DATA_DIR = "data/text"


def main_function():
    options = EnumeratedChooseOption(
        filter_list_dir_by_extensions(os.listdir(DATA_DIR), (".csv",))
    )
    conversation = Conversation(f"{DATA_DIR}/{options()}")

    conversation.stats()

    return Break() if input("Do you want to analyze another dataset? (y/n): ").lower() == "n" else Continue()


class TextAnalysis(Module):
    def __init__(self):
        super().__init__(main_function)
