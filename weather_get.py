import pandas as pd
import requests
from bs4 import BeautifulSoup
   
def request_data(link):

    page = requests.get(link)
    if page.status_code == 200:# 200 = ok
        soup= BeautifulSoup(page.content, 'html.parser')
        return soup

def get_weather_table(text):
    
    for tb in soup.find_all('table',  align="center", border="0", cellpadding="0", cellspacing="0", width="500"):
        result = [  [row.text.strip() for row in midd.find_all('font')] for midd in tb.find_all('tr', align="MIDDLE") if len(midd)==11  ]
        df = pd.DataFrame(result, columns=['DAY', 'DAILY_MIN', 'DAILY_MEAN', 'DAILY_MAX', 'PRECIPITATION'])
        df.reset_index(drop = True, inplace=True)
        return df
    
url = "http://thermo.karelia.ru/weather/w_history.php?town=kie&month=1&year=1881"
soup = request_data(url) #print(soup.prettify())
print(get_weather_table(soup))
