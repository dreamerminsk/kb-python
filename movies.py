from time import sleep

from functional import seq

from kb import get_movie
from kb.models import Movie, Person
from net import get_page
from store import get_films, save_person


def pm(m):
    return Movie(m[0], m[1], m[2], m[3])


def page(page):
    sleep(4)
    doc, e = get_page(get_movie(page))
    actors = []
    for actor_item in doc.select('span[itemprop=actor]'):
        save_person(Person(-1, actor_item.text.strip()))
        actors.append(actor_item.text.strip())
    return actors


movies = seq(get_films()).map(lambda m: pm(m)).flat_map(lambda m: page(m.page)).to_list()
print(movies)
