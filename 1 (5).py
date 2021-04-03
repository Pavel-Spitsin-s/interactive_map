import os
import pygame
import requests

SCREEN_W = 600
SCREEN_H = 530
COLORS = (0, 0, 0)
COORD = ["Капустин яр - 45.76, 48.57", "Байконур - 63.31, 45.62", "Восточный - 128.334405, 51.884058",
         "Ясный - 59.850274, 51.049437"]


def print__coord(lst):
    for i in lst:
        print(i)


pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen.fill(COLORS)
pygame.display.flip()
run = 1
font = pygame.font.Font(None, 20)
f2 = 1
m = ''
f3 = 0
print__coord(COORD)
while run:
    if f2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.KEYDOWN and 58 > event.key > 47:
                m += str(event.key - 48)
            if event.type == pygame.KEYDOWN and event.key == 44:
                m += ','
            if event.type == pygame.KEYDOWN and event.key == 46:
                m += '.'
            if event.type == pygame.KEYDOWN and event.key == 8:
                m = m[:-1]
            if event.type == pygame.KEYDOWN and event.key == 13:
                try:
                    f = m
                    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba" \
                                       "-98533de7710b&geocode=" + f + "&format=json&kind=house "
                    response = requests.get(geocoder_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    ind = toponym['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
                    f = toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
                    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
                    response = requests.get(geocoder_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    toponym_coodrinates = toponym["Point"]["pos"].split()
                    qwe = toponym['boundedBy']['Envelope']
                    w = list(map(float, qwe['lowerCorner'].split()))
                    q = list(map(float, qwe['upperCorner'].split()))
                    x = (q[0] - w[0]) / 2
                    c = (q[1] - w[1]) / 2
                    q = 'map'
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    f2 = 0
                except Exception as er:
                    f = m
                    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
                    response = requests.get(geocoder_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    json_response = response.json()
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    f = toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
                    ind = ''
                    geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + f + "&format=json"
                    response = requests.get(geocoder_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    json_response = response.json()
                    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                    toponym_coodrinates = toponym["Point"]["pos"].split()
                    qwe = toponym['boundedBy']['Envelope']
                    w = list(map(float, qwe['lowerCorner'].split()))
                    q = list(map(float, qwe['upperCorner'].split()))
                    x = (q[0] - w[0]) / 2
                    c = (q[1] - w[1]) / 2
                    qwe = x
                    qwe2 = c
                    q = 'map'
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    screen.blit(pygame.image.load(map_file), (0, 0))
                    f2 = 0
            screen.fill(COLORS)
            text = font.render(m, True, (240, 240, 240))
            screen.blit(text, (0, 0))
            pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 55 and event.pos[0] <= 123 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    q = 'sat'
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                if event.pos[0] >= 137 and event.pos[0] <= 185 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    q = 'map'
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                if event.pos[0] >= 191 and event.pos[0] <= 239 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    q = 'sat,skl'
                    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(
                        toponym_coodrinates) + "&spn=" + str(x) + ',' + str(c) + "&l=" + q
                    response = requests.get(map_request, params={
                        "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                if event.pos[0] >= 259 and event.pos[0] <= 307 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    f2 = 1
                if event.pos[0] >= 317 and event.pos[0] <= 375 and event.pos[1] >= 460 and event.pos[1] <= 480:
                    if not f3:
                        f3 = 1
                    else:
                        f3 = 0
            if event.type == pygame.KEYDOWN and event.key == 276 and float(toponym_coodrinates[0]) > 0.5:
                toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) - 0.05)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request, params={
                    "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 275 and float(toponym_coodrinates[0]) < 179.5:
                toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) + 0.05)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request, params={
                    "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN:
                toponym_coodrinates[1] = str(float(toponym_coodrinates[1]) - 0.025)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request, params={
                    "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 274 and float(toponym_coodrinates[1]) > 0.5:
                toponym_coodrinates[1] = str(float(toponym_coodrinates[1]) - 0.025)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request, params={
                    "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.KEYDOWN and event.key == 273 and float(toponym_coodrinates[1]) < 89.5:
                toponym_coodrinates[1] = str(float(toponym_coodrinates[1]) + 0.025)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request, params={
                    "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] < 440:
                toponym_coodrinates[1] = str(float(toponym_coodrinates[1]) - (event.pos[1] - 300) / 9000 / qwe)
                toponym_coodrinates[0] = str(float(toponym_coodrinates[0]) + (event.pos[0] - 220) / 18000 / qwe2)
                map_request = "http://static-maps.yandex.ru/1.x/?ll=" + ",".join(toponym_coodrinates) + "&spn=" + str(
                    x) + ',' + str(c) + "&l=" + q
                response = requests.get(map_request, params={
                    "pt": "{0},pm2dgl".format("{0},{1},{2}".format(m.split(',')[0], m.split(',')[1], 'pm2orm'))})
                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
        pygame.draw.rect(screen, (39, 42, 46), [(55, 460), (68, 20)])
        text = font.render("Спутник", True, (240, 240, 240))
        screen.blit(text, (59, 462))
        pygame.draw.rect(screen, (39, 42, 46), [(133, 460), (48, 20)])
        text = font.render("Схема", True, (240, 240, 240))
        screen.blit(text, (137, 462))
        pygame.draw.rect(screen, (39, 42, 46), [(191, 460), (58, 20)])
        text = font.render("Гибрид", True, (240, 240, 240))
        screen.blit(text, (195, 462))
        pygame.draw.rect(screen, (39, 42, 46), [(259, 460), (48, 20)])
        text = font.render("Поиск", True, (240, 240, 240))
        screen.blit(text, (263, 462))
        pygame.draw.rect(screen, (39, 42, 46), [(317, 460), (58, 20)])
        text = font.render("Индекс", True, (240, 240, 240))
        screen.blit(text, (321, 462))
        if f3:
            text = font.render(f"Индекс: {ind}", True, (240, 240, 240))
            screen.blit(text, (385, 462))
        else:
            pygame.draw.rect(screen, COLORS, [(385, 460), (100, 20)])
        text = font.render(f, True, (240, 240, 240))
        screen.blit(text, (60, 500))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
pygame.quit()
os.remove(map_file)
