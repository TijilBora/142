from bs4 import BeautifulSoup
import requests
import pandas as pd
page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
soup = BeautifulSoup(page.content, "html.parser")

star_table = soup.find_all('table')
temp_list = []
table_rows = star_table[7].find_all('tr')
print(table_rows[1])
for tr in table_rows:
    td=tr.find_all('td')

    row = [i.text.rstrip() for i in td]

    temp_list.append(row)


star_names = []
distance = []
mass = []
radius  = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])

print(df2)

df2.to_csv("Bright_stars.csv")



