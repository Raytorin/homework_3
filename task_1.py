from pip._vendor import requests

from pprint import pprint

def character_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    return response.json()

def max_intelligence(all_list):
    all_intelligence = []
    for loop_1 in all_list:
        all_intelligence.append(loop_1[1])
    top_intelligence = max(all_intelligence)
    for loop_2 in all_list:
        if top_intelligence == loop_2[1]:
            correct_character = loop_2[0]
    return print(f'Самый умный персонаж: {correct_character}')
    

if __name__ == '__main__':
    character = ['Hulk', 'Captain America', 'Thanos']
    character_list = []
    for full_dict in character_request():
        for need_character in character:
            if full_dict['name'] == need_character:
                character_list.append([full_dict['name'], full_dict['powerstats']['intelligence']])
    max_intelligence(character_list)