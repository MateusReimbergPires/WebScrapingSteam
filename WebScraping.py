# Este código realiza web scraping de um site de venda de facas e extrai informações específicas, como título, quantidade e preço.
# Os dados são armazenados em um arquivo CSV para posterior análise.

# Bibliotecas 
from bs4 import BeautifulSoup
import requests  
import pandas as pd
import datetime 

# Classe
class WebScraping():
    
    # Metodos
    def __init__(self, url):
        self.url = url
        self.soup = self.get_html() # Obtem o HTML da pagina web.

    def get_html(self):
        req = requests.get(self.url) # Faz a requisicao HTTP para obter o HTML da pagina web.
        soup = BeautifulSoup(req.content, "html.parser") # Cria um objeto no BeautifulSoup para analisar o HTML.
        return soup
    
    def get_knife(self): 
        return self.soup.find_all("a", class_ = "market_listing_row_link") # Retorna as Facas. 

    def get_title(self, knife):
        return knife.find("span", class_ = "market_listing_item_name").text # Retorna os nomes das Facas.
    
    def get_quantity(self, knife):
        return knife.find("span", class_ = "market_listing_num_listings_qty").text # Retorna a quatidade a venda no mercado.
    
    def get_price(self, knife):
        return knife.find("span", class_ = "market_table_value normal_price").find("span", class_ = "normal_price").text # Retorna o valor mais barato.

    def pick_all_knifes(self):
        df_rows = []
        for knife in self.get_knife():
            df_rows.append({ # Adiciona as informações da faca em um dicionário e o acrescenta na lista df_rows.
                'data': datetime.date.today(),
                'title':self.get_title(knife),
                'quantity':self.get_quantity(knife),
                'price':float(self.get_price(knife).replace('USD', '').replace("$","").replace(',','').strip()),
            })
        df = pd.DataFrame(df_rows) # Cria um DataFrame a partir da lista.
        df.to_csv("demo.csv") # Salva os dados em um arquivo CSV.
        return pd.DataFrame(df_rows) # Retorna um DataFrame com os dados extraídos.
