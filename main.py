from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
empire_page = response.text


soup = BeautifulSoup(empire_page, "html.parser")
movie_titles = [title.getText() for title in reversed(soup.find_all("h3", class_="title"))]


with open("must_watch_movies", "w", encoding="utf-8") as movies_file:
    for title in movie_titles:
        if title == "The Godfather":
            title = f"1) {title}"
        movies_file.write(f"{title}\n")

