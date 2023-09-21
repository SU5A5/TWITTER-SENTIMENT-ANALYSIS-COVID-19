# Assuming X_train is your training data
from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer()
count_vectorizer.fit(X_train)

# Save the CountVectorizer
with open('count_vectorizer.pkl', 'wb') as file:
    pickle.dump(count_vectorizer, file)
