import pandas as pd
from cli import ListElements


class Conversation:
    def __init__(self, csv_location):
        self.dataset = pd.read_csv(csv_location)
        self.word_freq = self.dataset['Content'].str.split(expand=True).stack().value_counts()
        self.author_freq = self.dataset['Author'].value_counts()
        self.messages_length_by_author = self.dataset.groupby('Author')['Content']\
            .apply(lambda x: x.str.len().mean()).apply(lambda x: round(x, 2))
        self.chars_by_author = self.dataset.groupby('Author')['Content'].apply(lambda x: x.str.len().sum())

    def print_stats(self):
        print("")
        options = ListElements([
            f"Total messages: {len(self.dataset)}",
            f"Total words: {self.word_freq.sum()}",
            f"Total unique words: {len(self.word_freq)}",
            f"Total authors: {len(self.author_freq)}",
            f"Average message length: {self.dataset['Content'].str.len().mean()}",
            f"Average words per message: {self.word_freq.mean()}",
            f"Average messages per author: {self.author_freq.mean()}",
            f"Average message length by author: {self.messages_length_by_author.to_dict()}",
            f"Total characters by author: {self.chars_by_author.to_dict()}"
        ])
        options()
        print("")
