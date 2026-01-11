import requests
from bs4 import BeautifulSoup
# Specify the URL of the webpage you want to scrape
url = 'https://freemoviesfull.cc/'
# Send an HTTP GET request to the webpage
response = requests.get(url)
# Store the HTML content in a variable
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.h1.text)
# Display a snippet of the HTML content
# print(html_content)


# other methods to do webscraping are :
# using scrapy which is open source frame work to do so 
# selenium as well