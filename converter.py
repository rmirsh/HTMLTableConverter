from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

page = requests.get('https://en.wikipedia.org/wiki/List_of_the_largest_software_companies')
soup = bs(page.text, 'html.parser')
table = soup.find("table", class_="wikitable sortable plainrowheads")
companies = table.find_all('th')
companies_titles = [title.text.strip() for title in companies]
column_data = table.find_all('tr')


df = pd.DataFrame(columns=companies_titles)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    df_len = len(df)
    df.loc[df_len] = individual_row_data

df.to_csv(r'/Users/kamilayupov/Devel/MyProjects/HTMLTableConverter/files/data.csv', 
          index=False)

if __name__ == "__main__":
    print(df)
