import requests
from bs4 import BeautifulSoup

def scrape_amazon_best_sellers(category):
    url = f"https://www.amazon.com/s?k={category.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = [item.text.strip() for item in soup.select(".s-title")]
    return products[:5]  # Return top 5 products based on preference

if __name__ == "__main__":
    category = input("Enter product category (e.g., Smartphones, Laptops): ")
    print(scrape_amazon_best_sellers(category))
