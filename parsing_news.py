import requests
from bs4 import BeautifulSoup

x = 0
while True:
    if x == 0:
        url = "https://news.ycombinator.com/newest"
    else:
        url = "https://news.ycombinator.com/newest" + nexx


    request = requests.get(url)

    soup = BeautifulSoup(request.text, "html.parser")

    theme = soup.find_all("td", class_="title")

    for themes in theme:
        themes = themes.find("a", {'class':'storylink'})
        if themes is not None and 'github.com' in str(themes):
            sublink = themes.get('href')
            print(str(themes.text) + ' ' + str(sublink))
            print("===")

    nex = soup.find(class_="morelink")
    nexlink = nex.get('href')

    nexx = nexlink[6:]
    x = x+1
