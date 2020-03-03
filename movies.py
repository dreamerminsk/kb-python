from functional import seq

from kb import get_movie
from kb.models import Movie
from net import get_page
from store import get_films

movies = get_films()


def pm(m):
    return Movie(m[0], m[1], m[2], m[3])


def page(page):
    return get_page(get_movie(page))


movie = seq(movies).map(lambda m: pm(m)).map(lambda m: page(m.page)).first()
print(movie)
