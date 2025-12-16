import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_excel("gen_ai_data.xlsx")
df.fillna("", inplace=True)

# Replace 'description' with the correct column name from your Excel
text_column = "description"  

tfidf = TfidfVectorizer(stop_words="english")
vectors = tfidf.fit_transform(df[text_column])

def recommend(query, top_n=5):
    query_vec = tfidf.transform([query])
    scores = cosine_similarity(query_vec, vectors).flatten()
    top_indices = scores.argsort()[-top_n:][::-1]

    results = []
    for i in top_indices:
        results.append({
            "text": df.iloc[i][text_column],
            "score": round(float(scores[i]), 3)
        })

    return results

