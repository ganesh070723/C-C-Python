import bs4
import instagram
import requests

user = {}
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_html = response.text
soup = bs4.BeautifulSoup(web_html, "html.parser")

movie=soup.findAll(name="h3",class_="jsx-4245974604")
print(movie)
