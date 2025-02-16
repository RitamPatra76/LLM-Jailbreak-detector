import pandas as pd
import numpy as np
import nltk
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv("dataset.csv")

# Preprocessing the input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text) 
    return text

df["prompt_text"] = df["prompt_text"].apply(clean_text)

# Building the Pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))), 
    ("classifier", MultinomialNB())
])
model.fit(X, y)
# Save model
with open("jailbreak_detector.pkl", "wb") as f:
    pickle.dump(model, f)
