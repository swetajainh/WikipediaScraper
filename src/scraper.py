import requests
import json
from bs4 import BeautifulSoup
import os

url='https://country-leaders.onrender.com'
# check the status code, if 200-it can connect to the endpoint
r=requests.get('https://country-leaders.onrender.com/status')
print(r.status_code)

# Function to get the cookie value
def get_cookie_value():
 cookies_url='https://country-leaders.onrender.com/cookie'
 cookie=requests.get(cookies_url)
 return cookie.cookies.get('user_cookie',' ' )

cookie_value= get_cookie_value()
# Query the endpoint, set the cookies variable, and display it
countries_endpoint= requests.get('https://country-leaders.onrender.com/countries',cookies={'user_cookie':cookie_value})
countries= countries_endpoint.json()
print(countries_endpoint.status_code)
print('countries= ',countries)

# open the url on chrome
#driver = webdriver.Chrome()
#driver.get(url)


# Set the leaders_url variable
leaders_url='https://country-leaders.onrender.com/leaders'
parameter = {
 "country1": "us", "country2": "be","country3":"ru","country4":"ma","country5":"fr"}
    

# query the /leaders endpoint, assign the output to the leaders variable 
# loop over the parameter to get leaders from all the country
# parameter.items iterate over both key and values
# the 'params' parameter is used when making HTTP GET requests to specify query
# parameters to be included in the URL
get_leaders=[]
for country,code in parameter.items():
  leaders=requests.get(leaders_url,params={"country":code},cookies={"user_cookie":cookie_value})
  leaders_per_country=leaders.json()
  # Accumulate leader details for all countries
  # extend() iterates for each arguement and extends the list
  get_leaders.extend(leaders_per_country)
  

# Extracting url of the leaders
def get_wikipedia_urls(leaders_per_country):
 wikipedia_urls = []
 for leader in leaders_per_country:
   wikipedia_url = leader.get('wikipedia_url')
   if wikipedia_url:
    wikipedia_urls.append(wikipedia_url)
 return wikipedia_urls

 #Extracting first paragraph
def get_first_paragraph(wikipedia_url):
    response = requests.get(wikipedia_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraph = soup.find_all('p')
    for para in paragraph:
        if len(para.text) > 100:
         return para.text
         break
    else:
      print('no paragraph found')
      
wikipedia_urls = get_wikipedia_urls(leaders_per_country)
for url in get_wikipedia_urls(get_leaders):
 first_paragraph = get_first_paragraph(url)
 print(first_paragraph)


all_leader_details = []
for leader in get_leaders:
    wikipedia_url = leader.get('wikipedia_url')
    if wikipedia_url:
        first_paragraph = get_first_paragraph(wikipedia_url)
        leader['first_paragraph'] = first_paragraph
        all_leader_details.append(leader)
    
leaders_data = json.dumps(all_leader_details, separators=(',\n', ': '))
#print(leaders_data)

file_path = "leader_data.json"
directory = os.path.dirname(file_path)
with open(file_path, "w") as json_file:
    json.dump(all_leader_details, json_file, indent=4)
