# ArXiv RSS
A quick script for creating an OPML file with RSS (really, Atom) feeds for all the authors you want to follow on arXiv. 
Create a list (saved as `authors.csv`) of the authors you'd like to follow (one on each line), with the first line as 'authorname'.

Usage: `python authorlist_to_rsslist.py > opml.xml`

It creates a file that can be uploaded to many RSS readers, such as Feedly, for them to automatically populate the relevant feeds for you. 
It is useful to keep a feed for each author loaded separately so that we can unsubscribe from individuals (if we want to) instead of having to mess with the arXiv API query every time.