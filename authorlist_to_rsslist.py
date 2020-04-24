"""
A quick script for creating an OPML file with RSS (really, Atom) feeds for all the authors you want to follow on arXiv. 
Create a list (saved as authors.csv) of the authors you'd like to follow (one on each line).

Usage: python authorlist_to_rsslist.py > authors.xml

It creates a file that can be uploaded to many RSS readers, such as Feedly, for them to automatically populate the relevant feeds for you. 
It is useful to keep a feed for each author loaded separately so that we can unsubscribe from individuals (if we want to) instead of having to mess with the arXiv API query every time.
"""

import pandas as pd

pd.set_option('display.max_colwidth', None)

OPML_HEADER = \
"""<?xml version="1.0" encoding="UTF-8"?>

<opml version="1.0">
    <head>
        <title>S subscriptions in feedly Cloud</title>
    </head>
    <body>
        <outline text="ArXiv Feed" title="ArXiv Feed">"""

OPML_ENDING = \
"""        </outline>
    </body>
</opml>"""

def get_arxiv_query(author_name: str)->str:
    author_name_list = author_name.split(' ')
    author_name_query = '+'.join(author_name_list)
    abbrev_name = author_name.split(' ')
    abbrev_name = [abbrev[0] if index != len(abbrev_name)-1 else abbrev for index, abbrev in enumerate(abbrev_name)]
    abbrev_name_query = '+'.join(abbrev_name)
    return f'http://export.arxiv.org/api/query?search_query=au:%22{author_name_query}%22+OR+au:%22{abbrev_name_query}%22&sortBy=submittedDate&sortOrder=descending&max_results=100'.replace('&', '&amp;')

def get_opml_lines(data: pd.Series)->pd.Series:
    opml_line = f"""<outline type="rss" text="{data.authorname}" title="{data.authorname}" xmlUrl="{data.queries}"/>"""
    return " "*12 + opml_line


def main():
    authors_filename = 'authors.csv'
    author_data = pd.read_csv('authors.csv', sep='\n', dtype=str, header=None, names=['authorname'])
    author_data['queries'] = author_data.authorname.apply(get_arxiv_query)
    opml_lines = author_data.apply(get_opml_lines,axis=1)

    print(OPML_HEADER)
    print(str(opml_lines.str.cat(sep='\n')))
    print(OPML_ENDING)
    
    return
    


if __name__ == "__main__":
    main()