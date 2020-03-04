from functional import seq

from kb import get_movie
from kb.models import Movie
from net import get_page
from store import get_films


def pm(m):
    return Movie(m[0], m[1], m[2], m[3])


def page(page):
    doc, e = get_page(get_movie(page))
    actors = []
    for actor_item in doc.select('span[itemprop=actor]'):
        actors.append(actor_item.text)
    return actors


movie = seq(get_films()).map(lambda m: pm(m)).map(lambda m: page(m.page)).first()
print(movie)
