from bs4 import BeautifulSoup
import requests

url = 'https://stormsoft.com.br/'
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('h2')

    for title in titles:
        print(title.text)

else:
    print("Falha ao acessar a página.")

