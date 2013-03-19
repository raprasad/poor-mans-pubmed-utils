import sys
import json
import pprint, urllib
from entrez_settings import ENTREZ_UTIL_API_KEY, ENTREZ_URL_EFETCH_BASE, PROXIES
from utils.msg_util import *

def pull_article_by_pmid(pubmed_id):
    msgt('pull_article_by_pmid: %s' % pubmed_id)
    # http://www.ncbi.nlm.nih.gov/pubmed/22969706
    #
    params = urllib.urlencode({'db': 'pubmed', 'id': pubmed_id, 'apikey': ENTREZ_UTIL_API_KEY}) 
    msg('params: %s' % params)
    
    url_str = '%s?%s' % (ENTREZ_URL_EFETCH_BASE, params)

    msg(url_str)

    # open url
    f = urllib.urlopen(url_str, proxies=PROXIES)

    # read in content
    pubmed_str = f.read()
    #print pubmed_str
    # convert to JSON
    #pubmed_json = json.loads(pubmed_str)

    # print in human readable format, indent is 4 spaces
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(pubmed_json)

    return pubmed_str
    
    
if __name__=='__main__':
    if len(sys.argv) == 2:
        pull_article_by_id(sys.argv[1])
    else:
        print 'python pull_article_by_pmid.py [pubmed id number]'
