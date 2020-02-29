from typing import Dict

urls: Dict[str, str] = {
    'year': 'http://kinobusiness.com/kassovye_sbory/films_year/',
    'weekends': 'http://kinobusiness.com/kassovye_sbory/weekend/',
    'thursdays': 'http://kinobusiness.com/kassovye_sbory/thursday/'
}


def getweekend(date):
    return '{0}{1}/{2}/'.format(urls['weekends'], date.strftime('%Y'), date.strftime('%d.%m.%Y'))
