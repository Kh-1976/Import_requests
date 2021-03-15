import requests

lst_heroes = ['Hulk', 'Captain America', 'Thanos']


def intelligence_max(lst_heroes):
    url = "https://superheroapi.com/api/2619421814940190/search/"
    max_intelligence, hero = 0, ''
    for i in lst_heroes:
        url_hero = url + i
        resp = requests.get(url_hero)
        lst_hero = resp.json()['results']
        if int(lst_hero[0]['powerstats']['intelligence']) > max_intelligence:
            max_intelligence = int(lst_hero[0]['powerstats']['intelligence'])
            hero = i
    return hero


print(intelligence_max(lst_heroes))
