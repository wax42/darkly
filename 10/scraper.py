from bs4 import BeautifulSoup
import requests
import re
import sys

flag = ""

def loop(i, path):
    global flag
    url = path
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    a = content.find_all('a', href=True)

    # print("LEN LINK = ", len(a), "i{:d}".format(i), "{:s}".format(url))
    for link in a: 
        if (link['href'] == "README"):
            res = requests.get(url + "README")
            c = str(BeautifulSoup(res.content, "html.parser"))
            if (re.match(".*Demande.*", c) != None or re.match(".*voisin.*", c) != None or re.match(".*aide.*", c) != None or re.match(".*craquer.*", c) != None or re.match(".*toujours.*", c) != None):
                pass
            else:
                print("FLAG : ", c)
                sys.exit(0);
        if (link["href"] != "../"):
            loop(i + 1, url + link['href'])


loop(1, "http://10.11.200.169/.hidden/")
