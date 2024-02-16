import requests
import json
from bs4 import BeautifulSoup
import os
from src.scraper import Country_Leaders


if __name__ == "__main__":
    country_leaders = Country_Leaders()
    
    # Refresh cookie and get countries
    cookie = country_leaders.refresh_cookie()
    print("Cookie:", cookie)
    countries = country_leaders.countries()
    print("Supported countries:", countries)

    

    # Get the first paragraph for the first leader (assuming there is at least one leader)
    if country_leaders.leadersdata:
        wikipedia_url = country_leaders.leadersdata[0].get('wikipedia_url')
        if wikipedia_url:
            first_paragraph = country_leaders.get_first_paragraph(wikipedia_url)
            print("First paragraph:", first_paragraph)

    # Save leader data to a JSON file
    country_leaders.to_json_file("leader_data")
    


    