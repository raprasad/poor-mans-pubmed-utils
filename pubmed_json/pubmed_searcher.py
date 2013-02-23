"""
esearch function

"""
import json
import urllib
import pprint
from entrez_settings import ENTREZ_UTIL_API_KEY, ENTREZ_URL_SEARCH_BASE
from utils. msg_util import *

class PubmedSearchResult:
    """
    Take the result of a pubmed search (JSON in string format ) and pulls out:
        - result count
        - list of PubMed IDs 
    """
    def __init__(self, json_str):
        self.pubmed_json = None
        self.num_results = 0
        self.pubmed_ids = []
        self.err_msgs = []

        self.parse_pubmed_json(json_str)

    def add_err_msg(self, msg_str):
        msg(msg_str)
        self.err_msgs.append(msg_str)

    def parse_pubmed_json(self, json_str):
        msg('parse_pubmed_json')
        
        if json_str is None:
            self.add_err_msg('parse_pubmed_json. json_str is None')
            return
        
        # convert to JSON
        try:
            self.pubmed_json = json.loads(json_str)
        except:
            self.add_err_msg('parse_pubmed_json. failed to convert json_str to JSON')
            return

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.pubmed_json)

        try:
            self.num_results = int(self.pubmed_json['result']['Count'])
        except:
            self.add_err_msg('parse_pubmed_json. failed to find result count')
            return 
            
        if self.num_results <= 0:
            self.add_err_msg('parse_pubmed_json. No results')
            return
            
        try:
            pmid_ids = self.pubmed_json['result']['IdList']
        except:
            self.add_err_msg('parse_pubmed_json. failed to IdList with PubMed IDs')
            
        for pm_id in pmid_ids:
            self.pubmed_ids.append(pm_id)
        
def search_by_author(author_name, result_dir):
    search_by_author_list(author_names=[author_name])
    
def search_by_author_list(author_names=["Sanes R"], return_max=300):

    #if not os.path.isdir(result_dir):
    #    os.makedirs(result_dir)
    
    fmt_authors = []
    author_names = map(lambda x: x.strip(), author_names)
    for a in author_names:
        fmt_authors.append('%s[Author]' % a.strip())
    
    search_term = ' AND '.join(fmt_authors)
    msg('search_term: %s' % search_term)
    
    # parameters for pulling this pubmed article in JSON format
    # http://www.ncbi.nlm.nih.gov/pubmed/22969706
    #
    params = urllib.urlencode({'db': 'pubmed'\
                , 'apikey': ENTREZ_UTIL_API_KEY\
                , 'retmax' : return_max\
                , 'term' : search_term
                }) 

    url_str = '%s?%s' % (ENTREZ_URL_SEARCH_BASE, params)

    msg('search url: %s' % url_str)

    # open url
    f = urllib.urlopen(url_str)

    # read in content
    pubmed_str = f.read()

    sr = PubmedSearchResult(pubmed_str)

    #print sr.pubmed_ids
    return sr
    
    
if __name__=='__main__':
    #search_by_author(author_name="Sanes JR", result_dir='sanes_pubs')
    search_by_author_list(author_names=['Finski', 'MacBeath'])#, result_dir='test')
    #search_by_author(author_name="Sanes JR", result_dir='test')
    #Apel
    
    #search_by_author(author_name="Engert F", result_dir='engert_pubs')
    #search_by_author(author_name="Hunter CP", result_dir='hunter_pubs')
    #search_by_author(author_name="Murray AW", result_dir='murray_pubs')
    #if len(sys.argv) == 2:
    #    search_by_author(sys.argv[1])
    #else:
    #    print '

