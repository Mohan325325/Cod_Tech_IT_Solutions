from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def scrape_news(request):
    url = 'https://example.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h2', class_='headline')

    context = {
        'headlines': headlines,
    }

    return render(request, 'scraper_app/news.html', context)
