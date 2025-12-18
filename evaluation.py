from recommender import recommend

def precision_at_k(recommended, relevant, k=5):
    recommended_k = recommended[:k]
    hits = sum(1 for item in recommended_k if item in relevant)
    return hits / k


if __name__ == "__main__":
    # Manual evaluation (acceptable for internship task)
    query = "cognitive ability test"
    relevant_products = ["Verify G+", "General Ability Test"]

    results = recommend(query, top_k=5)

    recommended_titles = [r["title"] for r in results]

    precision = precision_at_k(
        recommended_titles,
        relevant_products,
        k=5
    )

    print("Query:", query)
    print("Recommended:", recommended_titles)
    print("Relevant:", relevant_products)
    print("Precision@5:", precision)

