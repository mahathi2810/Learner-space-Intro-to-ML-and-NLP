import math
from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

corpus = [
    'the sun is a star',
    'the moon is a satellite',
    'the sun and moon are celestial bodies'
]

def preprocess(doc):
    return doc.lower().split()

processed_docs = [preprocess(doc) for doc in corpus]
vocabulary = sorted(set(word for doc in processed_docs for word in doc))

def compute_tf(doc, vocab):
    tf = defaultdict(int)
    for word in doc:
        tf[word] += 1
    tf = {word: tf[word] / len(doc) for word in vocab}
    return tf

df = {word: sum(word in doc for doc in processed_docs) for word in vocabulary}

idf = {word: math.log(len(processed_docs) / df[word]) for word in vocabulary}

manual_tf_idf_scores = []
for doc in processed_docs:
    tf = compute_tf(doc, vocabulary)
    tf_idf = {word: tf[word] * idf[word] for word in vocabulary}
    manual_tf_idf_scores.append(tf_idf)

print("\n Manual TF-IDF Scores ")
manual_df = pd.DataFrame(manual_tf_idf_scores).fillna(0)
print(manual_df)

cv = CountVectorizer()
count_matrix = cv.fit_transform(corpus).toarray()
count_vocab = cv.get_feature_names_out()
count_df = pd.DataFrame(count_matrix, columns=count_vocab)

print("\n CountVectorizer Output ")
print(count_df)

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(corpus).toarray()
tfidf_vocab = tfidf.get_feature_names_out()
tfidf_df = pd.DataFrame(tfidf_matrix, columns=tfidf_vocab)

print("\n TfidfVectorizer Output ")
print(tfidf_df)
