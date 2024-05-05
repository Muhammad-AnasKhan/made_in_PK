import csv
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://madeinpakistan.guide/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div container with class 'card-container'
container = soup.find('div', class_='card-container')

# Find all anchor tags within the container
anchors = container.find_all('a')

# Extract href attributes from anchor tags
hrefs = [a.get('href') for a in anchors]

# Print the hrefs
print(hrefs)

# Function to scrape products from a given href page
def scrape_products(href):
    # Send a GET request to the href page
    response = requests.get(url+href)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <h3> tags within the class "alternative"
    products = soup.find_all('div', class_='alternative')
    
    # Extract the text from the <h3> tags
    product_names = [product.find('h3').text for product in products]
    
    return product_names


# Open a CSV file in write mode
with open('made_in_PK_products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'BoycotProduct', 'Alternatives'])
    for href in hrefs:
        print(f"processing: {url + href}")
        products = scrape_products(href)
        writer.writerow([url+href ,href.replace('/', ''), products])

print("Data saved to made_in_PK_products.csv")