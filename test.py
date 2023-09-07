import requests
from bs4 import BeautifulSoup
import time

# Read the list of Google Dorks from list.txt
with open('list.txt', 'r') as file:
    dorks = file.read().splitlines()

# Define a function to scrape Google search results
def scrape_google_dork_links(dork):
    url = f'https://www.google.com/search?q={dork}'
    headers = {'User-Agent': 'Your User-Agent Here'}  # Replace with your User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/url?q=')]
        # Remove the "/url?q=" prefix and decode URL encoding
        cleaned_links = [requests.utils.unquote(link[7:]) for link in links]
        return cleaned_links
    except Exception as e:
        print(f"An error occurred for '{dork}': {e}")
        return []

# Create a dictionary to store links for each dork
results_dict = {}

for dork in dorks:
    links = scrape_google_dork_links(dork)
    # Remove duplicates and sort alphabetically
    unique_sorted_links = sorted(list(set(links)))
    results_dict[dork] = unique_sorted_links
    # Slow down the scraping to be polite to Google
    time.sleep(1)  # You can adjust the sleep duration as needed

# Create a text file to save the scraped links
with open('scraped_links.txt', 'w') as output_file:
    for dork, links in results_dict.items():
        output_file.write(f"Dork: {dork}\n")
        for link in links:
            output_file.write(link + '\n')
        output_file.write('\n')

print("Scraping complete. Links saved to 'scraped_links.txt'")
