import wikipedia  # importing wiki pedia module
import requests  # importing request module
import string  # importing string
from bs4 import BeautifulSoup  # importing beautifull soup module

x="run"
while(x=="run"): # while this condition is true this code will run
    f = input("search: ")  # search any thing you want
    e = wikipedia.search(f)  # it will search for wekipedia web pages with similar name
    print(e)  # show all wekipedia web page with similar name
    print("which one is it search it below")

    Enter_input = input("search: ")  # enter the topic you want totes about
    lists = Enter_input.split()  # seperates the word
    word = "_".join(lists)  # add "_" between the words

    url = "https://en.wikipedia.org/wiki/" + word  # format of link of wikipedia
    
    y = 1
    while (y == 1):  # while this condition is true this code will run
        def wikibot(url):
            url_open = requests.get(url)  # opening the url
            soup = BeautifulSoup(url_open.content, "html.parser")  # display the content of the url
            details = soup("table", {"class": "infobox"})  # format in which the information shoud be displayed
            for i in details:
                h = i.find_all("tr")  # wekipedia is writen in html so
                # The <tr> HTML element defines a row of cells in a table
                for j in h:
                    heading = j.find_all("th")  # in html <th> tag defines a header cell in an HTML table
                    detail = j.find_all("td")  # The <td> tag defines a standard data cell in an HTML table
                    if heading is not None and detail is not None:  # if something is in heading and details then wxicute this
                        for x, y in zip(heading, detail):  # format in which heading and details will shown
                            print("{}  ::  {}".format(x.text, y.text))
                            print("")  # seperate every topic by ""
            for i in range(1, 3):
                print(soup("p")[i].text)
        wikibot(url)
        y=y-1