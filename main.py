import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soap = BeautifulSoup(response.text,"html.parser")


movies = soap.find_all(name="h3",class_="listicleItem_listicle-item__title__BfenH")
movie_list = []
for movie in movies:
    movie_list.append(movie.text)

movie_list = movie_list[::-1]

for movie in movie_list:
    print(movie)