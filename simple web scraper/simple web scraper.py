import requests
from bs4 import BeautifulSoup

def extract_data(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the data you need
    title = soup.find('h1').text
    paragraphs = [p.text for p in soup.find_all('p')]

    # Print the data
    print("Title:", title)
    print("Paragraphs:", paragraphs)

# Example usage:
url = input("Enter website link:")
extract_data(url)
