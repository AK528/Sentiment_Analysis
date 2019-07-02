VECTORIZER = None
DATAFILE = "sentiment_analysis/data/datafile/"


dataset = ['train.csv', 'test.csv']
"""
sentiment_class : It take classes as multi_class or binary_class depending on data.
"""

sentiment_class = "binary_class"

"""
feature_col : Feature use for training 
target : Target column
"""

feature_col = 'text'

target = 'sentiment'
