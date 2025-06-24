-  ⁠CountVectorizer shows high values for very common words like "the".
- TfidfVectorizer and manual TF-IDF give the word "the" a low score because it shows up in almost every sentence, so it doesn’t help tell the sentences apart.
-  ⁠Rare but meaningful words like "celestial" get higher TF-IDF scores.

---


-  ⁠Words like "the" appear in almost every sentence or document.
-  ⁠While they occur often (high count), they don’t give much unique information about the content.
-  ⁠TF-IDF reduces their importance* by multiplying their frequency by a low IDF score.
-  ⁠This is why "the" has a high score in CountVectorizer, but **a low score in both TF-IDF methods.

---


- ⁠CountVectorizer is useful when raw frequency matters.
-  ⁠TF-IDF is better for identifying meaningful words in documents, especially in NLP tasks like classification or search.

