import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

good_feedback = [
    "This product is amazing!", "Very satisfied with the purchase.", "Excellent quality.",
    "Fast delivery and great service.", "Highly recommend it to everyone.", "Five stars!",
    "Exceeded my expectations.", "Definitely worth the price.", "User-friendly and efficient.",
    "Fantastic experience overall."
] * 10  

bad_feedback = [
    "This product is terrible.", "Very disappointed with the quality.", "Not worth the money.",
    "Late delivery and poor service.", "Would not recommend to anyone.", "One star only.",
    "Failed to meet expectations.", "Totally overpriced.", "Confusing and hard to use.",
    "Worst purchase ever."
] * 10

texts = good_feedback + bad_feedback
labels = ['good'] * 100 + ['bad'] * 100

df = pd.DataFrame({'Text': texts, 'Label': labels})

vectorizer = TfidfVectorizer(max_features=300, stop_words='english', lowercase=True)
X = vectorizer.fit_transform(df['Text'])
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

def text_preprocess_vectorize(texts, vectorizer):
   
    return vectorizer.transform(texts)

new_texts = ["I absolutely loved the product!", "Worst thing I ever bought."]
vectorized_texts = text_preprocess_vectorize(new_texts, vectorizer)
predictions = model.predict(vectorized_texts)

for text, pred in zip(new_texts, predictions):
    print(f"'{text}' → Prediction: {pred}")
