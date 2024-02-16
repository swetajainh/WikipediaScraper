import requests
import json
from bs4 import BeautifulSoup
import os

class Country_Leaders():
    def __init__(self):
        self.leadersdata = []
        self.cookie_value = self.refresh_cookie()

    def refresh_cookie(self):
        cookies_url = 'https://country-leaders.onrender.com/cookie'
        cookie = requests.get(cookies_url)
        return cookie.cookies.get('user_cookie', '')

    def countries(self):
        countries_endpoint = requests.get('https://country-leaders.onrender.com/countries', cookies={'user_cookie': self.cookie_value})
        countries = countries_endpoint.json()
        return countries

    def get_leaders(self, country: str):
        leaders_url = 'https://country-leaders.onrender.com/leaders'
        parameter = {"country1": "us", "country2": "be", "country3": "ru", "country4": "ma", "country5": "fr"}
        for _, code in parameter.items():
            leaders = requests.get(leaders_url, params={"country": code}, cookies={"user_cookie": self.cookie_value})
            leaders_per_country = leaders.json()
            self.leadersdata.extend(leaders_per_country)

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        response = requests.get(wikipedia_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraph = soup.find_all('p')
        for para in paragraph:
            if len(para.text) > 100:
                return para.text
        return 'No paragraph found'

    def to_json_file(self, filepath: str):
        leader_details = []
        for leader in self.leadersdata:
            wikipedia_url = leader.get('wikipedia_url')
            if wikipedia_url:
                first_paragraph = self.get_first_paragraph(wikipedia_url)
                leader['first_paragraph'] = first_paragraph
            leader_details.append(leader)
        file_path = "leader_data"
        
        with open(file_path, "w") as json_file:
            json.dump(leader_details, json_file, indent=4)