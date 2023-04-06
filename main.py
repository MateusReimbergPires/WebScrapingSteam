from WebScraping import WebScraping

# Definicao do URL alvo para coleta dos dados.
url = "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=tag_weapon_knife_karambit&appid=730#p1_price_desc"
WebScraping = WebScraping(url) # Criando uma instancia da classe WebScraping com a URL
print(WebScraping.pick_all_knifes()) # Chamando o método pick_all_knifes() para coletar todas as facas disponíveis na página.

