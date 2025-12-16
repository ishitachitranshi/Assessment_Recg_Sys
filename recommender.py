import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_excel("gen_ai_data.xlsx")
df.fillna("", inplace=True)

# Automatically select the first text-like column if 'description' is not found
default_column = "description"
if default_column in df.columns:
    text_column = default_column
else:
    # Choose first column that has string type
    text_columns = df.select_dtypes(include=["object"]).columns
    if len(text_columns) == 0:
        raise ValueError("No text column found in the dataset!")
    text_column = text_columns[0]
    print(f"Column 'description' not found. Using '{text_column}' instead.")

# Create TF-IDF vectors
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

