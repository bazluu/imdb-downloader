from django.conf import settings

import requests


def get_movie_by_imdb_title_id(imdb_title_id: str):
    params = {"apikey": settings.OMDB_API_KEY, "i": imdb_title_id}
    movie_data = requests.get("http://www.omdbapi.com/", params=params).json()

    return movie_data
