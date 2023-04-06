# Projeto de Web Scraping - Análise de Facas Vendidas no Mercado da Steam
Este projeto é um web scraping que extrai informações específicas, como título, quantidade e preço, das Karambits vendidas no mercado da Steam, uma plataforma de jogos online. Os dados extraídos são armazenados em um arquivo CSV para análise posterior.

## Bibliotecas Utilizadas
- BeautifulSoup: Utilizada para fazer o parsing do HTML da página web e extrair os dados.
- Requests: Utilizada para fazer as requisições HTTP e obter o HTML da página web.
- Pandas: Utilizada para criar e manipular os DataFrames para armazenar e analisar os dados extraídos.
- Datetime: Utilizada para obter a data atual para adicionar como informação nos dados extraídos.

## Como Usar
1. Clone o repositório para o seu ambiente local.
2. Certifique-se de ter as bibliotecas mencionadas instaladas em seu ambiente Python.
3. Execute o arquivo Python do projeto.
4. Os dados extraídos serão armazenados em um arquivo CSV chamado "demo.csv" no mesmo diretório do projeto.

## Estrutura do Código
WebScraping: Classe principal do projeto que contém os métodos para realizar o web scraping e extrair as informações das facas.
- get_html(): Método que faz a requisição HTTP e obtém o HTML da página web.
- get_knife(): Método que retorna os elementos HTML que contêm as informações das facas.
- get_title(): Método que extrai o título das facas a partir do HTML.
- get_quantity(): Método que extrai a quantidade das facas a partir do HTML.
- get_price(): Método que extrai o preço das facas a partir do HTML.
- pick_all_knifes(): Método que itera sobre os elementos HTML das facas, extrai as informações e as armazena em um DataFrame e em um arquivo CSV.
