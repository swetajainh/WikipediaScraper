![alt text](image.png)

Description:
A scraper that builds a JSON file with the political leaders of each country you get from this API.
In this file the first paragraph of the Wikipedia page of these leaders is included. 

Repo Structure
src folder
![alt text](image-1.png) Scraper.py
![alt text](image-2.png) Main.py
![alt text](image-3.png) Readme.md

Usage
1. Clone the repository to your local machine.
2. To run the script, you can execute the main.py file from your command line:
3. Setup and preparation
Create a virtual environment using venv
Create a requirements.txt file with the required libraries (hint: pip freeze and pipreqs might be helpful here!)
4. The object should contain at least these five methods:

refresh_cookie() -> object returns a new cookie if the cookie has expired
get_countries() -> list returns a list of the supported countries from the API
get_leaders(country: str) -> None populates the leader_data object with the leaders of a country retrieved from the API
get_first_paragraph(wikipedia_url: str) -> str returns the first paragraph (defined by the HTML tag <p>) with details about the leader
to_json_file(filepath: str) -> None stores the data structure into a JSON file

Timeline
The project took three days for completion

Personal Situation
The project was done as a part of AI Bootcamp at BeCode.org