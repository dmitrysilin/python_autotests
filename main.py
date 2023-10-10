import requests
token = 'd952c172a3f3efce94ded3900b2b667a'
host = 'https://api.pokemonbattle.me:9104'
response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Dompokemon",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)

'''responce_change = requests.put('{host}/pokemons', json = {
    "pokemon_id": "12261",
    "name": "Dompokemon1",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_change.text)'''

'''responce_gacha = requests.post('{host}/trainers/add_pokeball', json = {
    "pokemon_id": "12261"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : 
              token } )

print(responce_gacha.text)'''