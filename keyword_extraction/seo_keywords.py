def get_keywords(product_name):
    # Placeholder for API call to Ubersuggest or Google Keyword Planner
    keywords = [product_name.lower(), "trending", "best-selling", "e-commerce"]
    return keywords[:4]

if __name__ == "__main__":
    product = "Wireless Headphones"
    print(get_keywords(product))
