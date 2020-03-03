from functional import seq

from kb.models import Movie
from store import get_films

movies = get_films()


def pm(m):
    return Movie(m[0], m[1], m[2], m[3])


movie = seq(movies).map(lambda m: pm(m)).first()
print(movie)
