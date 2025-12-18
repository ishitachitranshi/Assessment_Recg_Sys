import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.shl.com/products/product-catalog/"

def scrape_shl_products():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    for card in soup.select(".product-card"):
        title = card.select_one("h3")
        desc = card.select_one("p")

        products.append({
            "title": title.text.strip() if title else "",
            "description": desc.text.strip() if desc else ""
        })

    df = pd.DataFrame(products)
    df.to_csv("data/shl_products.csv", index=False)
    return df

if __name__ == "__main__":
    scrape_shl_products()
