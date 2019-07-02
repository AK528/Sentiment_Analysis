from sentiment_analysis.feature_extraction import feature_extraction
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sentiment_analysis import utility
from sentiment_analysis.config import target

class Model:
    def __init__(self):
        self.rf = RandomForestClassifier(n_jobs=-1)

    def split(self, train, datasets):
        return train_test_split(
            train, datasets[0][target], test_size=0.3, random_state=123
        )

    def training(self, X_train, X_test, y_train, y_test):
        self.rf.fit(X_train, y_train)
        predict = self.rf.predict(X_test)
        print("Accuracy", f1_score(y_test, predict, average="weighted"))

    def save(self):
        utility.save_instance(self.rf, './saved_instance/model')


if __name__ == "__main__":
    feature = feature_extraction.FeatureExtraction()
    vec = feature.vectorizer()
    train, test, datasets = feature.vector_transform(vec)
    model = Model()
    print("model")
    X_train, X_test, y_train, y_test = model.split(train, datasets)
    model.training(X_train, X_test, y_train, y_test)
    model.save()
