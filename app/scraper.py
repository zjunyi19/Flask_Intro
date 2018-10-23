import requests
from bs4 import BeautifulSoup

def parse():
    url = "https://caensoftware.engin.umich.edu/4"
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html,features="html.parser")
    table = soup.find('tbody',attrs={})
    rows = []
    for row in table.findAll('tr'):
        temp_row = []
        for cell in row.findAll('td'):
            output = cell.text.strip()
            temp_row.append(output)
        rows.append(temp_row)
    return [rows,['Software Title','Software Version Number','Operating System','Product Name','Remote Access On-Campus','Remote Access Off Campus','Restrictions']]

if __name__ == "__main__":
    print(parse())