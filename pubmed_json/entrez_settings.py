import config.my_config as config

ENTREZ_URL_ESEARCH_BASE = 'http://entrezajax.appspot.com/esearch'
ENTREZ_URL_EFETCH_BASE = 'http://entrezajax.appspot.com/efetch'

ENTREZ_UTIL_API_KEY = config.ENTREZ_UTIL_API_KEY    # key for http://entrezajax.appspot.com
PROXIES = config.PROXIES    # if proxies needed for pulling the url