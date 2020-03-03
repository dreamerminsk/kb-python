import logging.config

import requests
from bs4 import BeautifulSoup

logging.config.fileConfig('log.conf')
logger = logging.getLogger(__name__)

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})


def get_page(ref):
    logger.info(ref)
    try:
        r = s.get(ref, timeout=32)
        logger.info('{0} {1} {2}'.format(r.status_code, r.reason, r.elapsed))
        html = BeautifulSoup(r.text, 'html.parser')
        return html, None
    except Exception as ex:
        logger.error(ex)
        return None, ex
