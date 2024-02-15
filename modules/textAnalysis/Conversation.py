import pandas
import pandas as pd
from cli import ListElements


class Conversation:
    def __init__(self, csv_location):
        self.dataset = self.clean_discord_call_info(pd.read_csv(csv_location))
        self.word_freq = self.dataset['Content'].str.split(expand=True).stack().value_counts()
        self.word_freq_by_author = self.dataset.groupby('Author')['Content'].apply(lambda x: x.str.split(expand=True).stack().value_counts())
        self.author_freq = self.dataset['Author'].value_counts()
        self.messages_length_by_author = self.dataset.groupby('Author')['Content'] \
            .apply(lambda x: x.str.len().mean()).apply(lambda x: round(x, 2))
        self.chars_by_author = self.dataset.groupby('Author')['Content'].apply(lambda x: x.str.len().sum())

    @staticmethod
    def clean_noise_words_from_indexes(df: pd.DataFrame) -> pd.DataFrame:
        with open("data/noise_word_list_pl.txt", "r") as f:
            conjunctives = f.read().splitlines()

        for conjunctive in conjunctives:
            df = df[~df.index.str.fullmatch(conjunctive, case=False)]
        return df

    @staticmethod
    def clean_discord_call_info(df: pd.DataFrame, column="Content") -> pd.DataFrame:
        return df[~df[column].str.contains("Started a call", case=False, na=False)]

    def stats(self):
        print("")
        options = ListElements([
            f"Total messages: {len(self.dataset)}",
            f"Total words: {self.word_freq.sum()}",
            f"Most common words: {self.clean_noise_words_from_indexes(self.word_freq).head(40).to_dict()}",
            f"Most common words by author: {[self.clean_noise_words_from_indexes(self.word_freq_by_author[author]).head(40).to_dict() for author in self.word_freq_by_author.index.levels[0]]}",
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
