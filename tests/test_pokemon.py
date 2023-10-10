import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
id = '1934'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': {id}})
    assert response.status_code == 200

def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id': {id}})
    assert answer_body.json()['trainer_name'] == 'Domashka'