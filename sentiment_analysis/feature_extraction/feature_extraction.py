from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sentiment_analysis.data import dataloader
from sentiment_analysis.preprocessor import preprocessing
from sentiment_analysis import config
from sentiment_analysis.config import feature_col , target
from sentiment_analysis.utility import save_instance


class FeatureExtraction:
    def __init__(self):
        self.dataset = dataloader.DataLoader().load()
        for df in self.dataset:
            df.dropna(inplace=True)
            preprocess = preprocessing.PreProcessor(df)
            df[feature_col] = df[feature_col].apply(lambda x: preprocess.lemmatize(x))
            df["word_count"] = df[feature_col].apply(lambda x: len(x))
            df.drop(df[df["word_count"] == 0].index, inplace=True)
            df.reset_index(drop=True, inplace=True)

    def vectorizer(self, vectorizer=None,api=False):

        config.VECTORIZER = vectorizer

        if config.VECTORIZER is None:
            print('tfidf')
            vec = TfidfVectorizer(analyzer="word", max_df=0.8, stop_words="english")

        if config.VECTORIZER == "tf-idf":
            vec = TfidfVectorizer(analyzer="word", max_df=0.8, stop_words="english")

        if config.VECTORIZER == "countv":
            print('BOW')
            vec = CountVectorizer(
                analyzer="word", stop_words="english", ngram_range=(1, 2)
            )

        fitted = vec.fit(self.dataset[0][feature_col])
        save_instance(vec, './saved_instance/vectorizer')

        return fitted

    def vector_transform(self, vec):
        vec_train = vec.transform(self.dataset[0][feature_col])
        vec_test = vec.transform(self.dataset[1][feature_col])

        return vec_train, vec_test, self.dataset

    def make_prediction(self,vec,data):
        predict_vect = vec.transform(data)
        return predict_vect


if __name__ == "__main__":
    feature = FeatureExtraction()
    vec = feature.vectorizer()
    train, test, datasets = feature.vector_transform(vec)
    print(train.shape)
    print(test.shape)
