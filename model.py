import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from preprocess import clean_text

# Load data
df = pd.read_csv("expense.csv")

df['text'] = df['text'].apply(clean_text)

# Features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['category']

# Model
model = MultinomialNB()
model.fit(X, y)

# Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved!")