from sentiment_analysis.feature_extraction import feature_extraction
from sentiment_analysis.model import model


if __name__ == '__main__':
    feature = feature_extraction.FeatureExtraction()
    vec = feature.vectorizer()
    train, test, datasets = feature.vector_transform(vec)
    model = model.Model()
    print("model")
    X_train, X_test, y_train, y_test = model.split(train, datasets)
    model.training(X_train, X_test, y_train, y_test)
    model.save()





