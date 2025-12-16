import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_excel("gen_ai_data.xlsx")
df.fillna("", inplace=True)

# Automatically detect the first text column in dataset
text_col = df.select_dtypes(include='object').columns[0]

# Create TF-IDF vectors
tfidf = TfidfVectorizer(stop_words="english")
vectors = tfidf.fit_transform(df[text_col])


def recommend(query, top_n=5):
    """
    Returns top N recommended items based on cosine similarity.

    Parameters:
        query (str): Input text to search.
        top_n (int): Number of top recommendations to return.

    Returns:
        list of dicts: Each dict contains 'text' and 'score'.
    """
    query_vec = tfidf.transform([query])
    scores = cosine_similarity(query_vec, vectors).flatten()
    top_indices = scores.argsort()[-top_n:][::-1]

    results = []
    for i in top_indices:
        results.append({
            "text": df.iloc[i][text_col],
            "score": round(float(scores[i]), 3)
        })

    return results


