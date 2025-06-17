import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

positive_reviews = ["I loved this movie!", "Fantastic acting.", "Great direction!", 
                    "Absolutely amazing!", "Brilliant script.", "Loved the characters.",
                    "It was very enjoyable.", "A must watch!", "Incredible story.",
                    "Superb visuals."] * 5  

negative_reviews = ["I hated this movie.", "Terrible acting.", "Awful direction.", 
                    "Really boring.", "Bad script.", "Poor character development.",
                    "It was a waste of time.", "Would not recommend.", "Weak story.",
                    "Disappointing visuals."] * 5  

reviews = positive_reviews + negative_reviews
sentiments = ['positive'] * 50 + ['negative'] * 50

df = pd.DataFrame({
    'Review': reviews,
    'Sentiment': sentiments
})

vectorizer = CountVectorizer(max_features=500, stop_words='english')
X = vectorizer.fit_transform(df['Review'])  
y = df['Sentiment']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

def predict_review_sentiment(model, vectorizer, review):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)
    return prediction[0]

sample_review = "The movie was absolutely fantastic and thrilling!"
predicted_sentiment = predict_review_sentiment(model, vectorizer, sample_review)
print(f"Predicted Sentiment: {predicted_sentiment}")
