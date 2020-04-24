from bs4 import BeautifulSoup
import re
import time
import os


def treat(s):
    s = s.replace(u'Ã\xa0', 'à')
    s = s.replace(u'Ã¢', 'â')
    s = s.replace(u'Ã©', 'é')
    return s


os.system("cls")
html = open("musescore.html").read()
html = treat(html)
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")

if table == None:
    print("No table found. Make sure to have downloaded full HTML page.")
    time.sleep(2)
    quit()
else:
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for col in columns:
            a = re.sub(' +', ' ', re.sub('\n', '', col.text.strip()))
            if a != '':
                output_row.append(a)
        output_rows.append(output_row)

    total_views = 0
    total_lectures = 0
    total_dl = 0
    total_com = 0
    total_fav = 0

    views = dict()
    dow = dict()
    lect = dict()
    comm = dict()
    fav = dict()

    for row in output_rows:
        if len(row) > 0:
            nb = int(row[1])
            views[row[0]] = nb
            total_views += nb

            nb = int(row[2])
            lect[row[0]] = nb
            total_lectures += nb

            nb = int(row[3])
            dow[row[0]] = nb
            total_dl += nb

            nb = int(row[4])
            comm[row[0]] = nb
            total_com += nb

            nb = int(row[5])
            fav[row[0]] = nb
            total_fav += nb

    print("Total views : ", total_views)
    print("Total lectures : ", total_lectures)
    print("Total downloads : ", total_dl)
    print("Total comments : ", total_com)
    print("Total favorites : ", total_fav)

    most_viewed = max(views, key=views.get)
    print("\n\"" + most_viewed + "\" is the most viewed sheet with " +
          str(views[most_viewed]) + " views.")

    most_played = max(lect, key=lect.get)
    print("\"" + most_played + "\" is the most played sheet with " +
          str(lect[most_played]) + " plays.")

    most_dow = max(dow, key=dow.get)
    print("\"" + most_dow + "\" is the most downloaded sheet with " +
          str(dow[most_dow]) + " downloads.")

    most_com = max(comm, key=comm.get)
    print("\"" + most_com + "\" is the most commented sheet with " +
          str(comm[most_com]) + " comments.")

    most_fav = max(fav, key=fav.get)
    print("\"" + most_fav + "\" is the most favorited sheet with " +
          str(fav[most_fav]) + " favorites.")
