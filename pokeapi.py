import requests
import json

nome = "  bulbasaur".lower().strip()

def buscar_pokemon(nome):
    #pega a api e busca com base no nome {nome}
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    #faz a requisição com a url
    resposta = requests.get(url)
    #verifica o status, 200 = sucesso
    if resposta.status_code == 200:
        #transforma o json da api em dicionario
        dados = resposta.json()
        #faz as pesquisa no dicionario
        print(dados["name"])
        print(dados["height"])
        print(dados["types"][0]["type"]["name"])
    else:
        print("pokemon não encontrado")
    filtrar = {
        "nome": dados["name"],
        "altura": dados["height"],
        "tipo": dados["types"][0]["type"]["name"]
    }
    
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(filtrar, arquivo, indent=4)

buscar_pokemon(nome)
