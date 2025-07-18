from googlesearch import search

query = "Python programming"
for url in search(query, tld="com", lang="en", num=5, stop=5, pause=2):
    print(url)
