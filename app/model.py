import sklearn 
import pandas as pd 
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

lr = LinearRegression()

def train():
    df = pd.read_csv("comments_train.csv")
    df = df.reset_index(drop=True)
    df['sentiment'] = df['sentiment'].map({"Positive": 1, "Negative": 0})
    df.comment = df.comment.str.lower()
    # Pipeline creation
    X = df.comment
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1242)
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('clf', LogisticRegression())  # step2 - classifier
                         ])
    text_clf.fit(X_train, y_train)
    model = joblib.dump(text_clf, 'sentiment.pkl')
    return model
    
def check():
    try:
        with open('sentiment.pkl', 'rb') as fid:
            model = joblib.load(fid)
            return True
    except:
        return False

def predict(text):
# load it again
    model = check()
    if model:
         with open('sentiment.pkl', 'rb') as fid:
            model = joblib.load(fid)
    else:
        model = train()
    sentiment = model.predict([[text]])
    print(salary)
    return sentiment

#train()
#predict()
