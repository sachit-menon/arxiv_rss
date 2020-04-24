def get_queries(author_name: str)->str:
    author_name_list = author_name.split(' ')
    author_name_query = '+'.join(author_name_list)
    abbrev_name = author_name.split(' ')
    abbrev_name = [abbrev[0] if index != len(abbrev_name)-1 else abbrev for index, abbrev in enumerate(abbrev_name)]
    abbrev_name_query = '+'.join(abbrev_name)
    return '%22+OR+au:%22'.join([author_name_query, abbrev_name_query])

try:
    with open('authors.csv', 'r') as f:
        authorlist = f.read().splitlines()
except IOError:
    print("Error: File does not appear to exist.")

full_query = '%22+OR+au:%22'.join(map(get_queries, authorlist))

print('Your RSS feed is: \n' + f'http://export.arxiv.org/api/query?search_query=au:%22{full_query}%22&sortBy=submittedDate&sortOrder=descending&max_results=100'.replace('&', '&amp;'))