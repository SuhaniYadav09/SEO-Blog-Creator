from transformers import pipeline
from keyword_extraction.seo_keywords import get_keywords

def generate_blog_content(product):
    keywords = get_keywords(product)
    generator = pipeline("text-generation", model="gpt-3.5-turbo")
    prompt = f"Write a 150-word blog about {product} incorporating {', '.join(keywords)}."
    content = generator(prompt)
    return content[0]['generated_text']

if __name__ == "__main__":
    product = "Wireless Headphones"
    print(generate_blog_content(product))
