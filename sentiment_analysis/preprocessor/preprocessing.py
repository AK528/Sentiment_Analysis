import string
from collections import defaultdict


import pandas as pd
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction import text

from sentiment_analysis.data import dataloader
from sentiment_analysis.config import feature_col, target


class PreProcessor:

    def __init__(self, data=None):

        self.data = data
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize(self, phrase):

        filtered = []
        # phrase = re.sub('\[[^]]*\]', '', text)
        #     phrase=phrase.translate(None,string.punctuation)
        word_list = phrase.split()
        filtered = [self.lemmatizer.lemmatize(word).lower() for word in word_list if word not in string.punctuation]
        # print(filtered)
        return " ".join(filtered)
        # punctuations = string.punctuation
        # word_list = phrases.split()
        # for index in range(0, len(word_list)):
        #     pop_word = word_list.pop(0)
        #     if pop_word not in punctuations:
        #         if len(pop_word) > 3:
        #             word_list.append(self.lemmatizer.lemmatize(pop_word).lower())

        # return " ".join(word_list)

    def filter_word(self, phrases):
        phrase_sentiment = defaultdict(int)

        for phrase in phrases:
            for word in phrase.split():
                phrase_sentiment[word] += 1

        return phrase_sentiment



    def intersection(self, series_list):
        intersect = set(series_list[0])


        for series in series_list[1:]:
            intersect.intersection_update(series)

        comm_token = self.filter_word(intersect)
        _tokens = pd.Series([x for x in comm_token.keys()])
        print(_tokens.shape)
        return _tokens

    def stopword(self):
        sentiments = self.data[target].unique()
        series_list = []
        for sentiment in sentiments:
            phrase_sentiment = self.filter_word(
                df.loc[(df[target] == sentiment), "tidy_Phrase"].values
            )
            series_list[sentiment] = pd.Series(
                [key for key in phrase_sentiment.keys()]
            )

        common = self.intersection(series_list)
        my_stop_word = text.ENGLISH_STOP_WORDS.union(common)
        return my_stop_word

    @staticmethod
    def sentiment_label(_class):
        if _class == 'binary_class':
            return {0: "Negative", 1: "Positive"}
        elif _class == 'multi_class':
            return {0: "Highly negative", 1: "Somewhat negative", 2: "Neutral", 3: "Somewhat Positive",
                    4: "Highly Positive"}




if __name__ == "__main__":
    dataset = dataloader.DataLoader().load()
    for i, df in enumerate(dataset):
        print(df.columns)

        df.dropna(inplace=True)
        preprocess = PreProcessor(df)
        print(i)
        print('\n')

        df[feature_col] = df[feature_col].apply(lambda x: preprocess.lemmatize(x))
        df["word_count"] = df[feature_col].apply(lambda x: len(x))
        df.drop(df[df["word_count"] == 0].index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        print(df.columns)

        if target in df.columns:

           stop_word =  preprocess.stopword()

