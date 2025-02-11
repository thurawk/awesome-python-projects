import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
base_url = "http://quotes.toscrape.com/"

# Lists to store quotes, authors, and tags
all_quotes = []
all_authors = []
all_tags = []

# Step 1: Loop through all pages
current_page = base_url
while current_page:
    response = requests.get(current_page)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to access {current_page}. Status code:", response.status_code)
        break
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract quotes and authors on the current page
    quotes = [quote.text.strip() for quote in soup.find_all("span", class_="text")]
    authors = [author.text.strip() for author in soup.find_all("small", class_="author")]
    
    # Extract tags for each quote
    for quote_box in soup.find_all("div", class_="quote"):
        tags = [tag.text.strip() for tag in quote_box.find_all("a", class_="tag")]
        all_tags.append(", ".join(tags))  # Combine tags into a single string for each quote
    
    # Add to the main lists
    all_quotes.extend(quotes)
    all_authors.extend(authors)
    
    # Find the link to the next page
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.find("a")["href"]
        current_page = base_url + next_page
    else:
        current_page = None  # Exit the loop if no next page is found

# Step 2: Save the data into a DataFrame
data = {"Quote": all_quotes, "Author": all_authors, "Tags": all_tags}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("all_quotes_with_tags.csv", index=False, encoding='utf-8')

print("Data has been successfully saved to 'all_quotes_with_tags.csv'.")
