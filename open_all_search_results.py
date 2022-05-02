from ast import Num
import requests, sys, webbrowser, bs4

print("Searching ")
res = requests.get('URL' + ' '.join(sys.argv[1:]))
res.raise_for_status()

##retrieve top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('a')
print(linkElems)

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = linkElems[i].get('href')
    print('Opening ' + urlToOpen)
    webbrowser.open(urlToOpen)

    