from lib import download_webpage as dl
from lib import parse_webpage as parser

url = 'https://www.nba.com'

url_id = dl.download_url(url, 0)
parser.parse_url(url_id, 0)