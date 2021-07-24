from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")
movie_titles = [movie.text for movie in soup.find_all(name="h3", class_="title")][::-1]

with open("movies.txt", mode="w") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
