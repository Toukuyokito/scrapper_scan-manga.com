import requests
import sqlite3
import re

from bs4      import BeautifulSoup

import core.modele 

def __get_technical_div(url:str) -> str:
    web_page = requests.get(url, headers={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"})
    soup     = BeautifulSoup(web_page.content, "html.parser")
    return str(soup.find('div',attrs={'class': 'contenu_fiche_technique border_radius_contener folder_corner'}))


def __isolate_episode_number(data:str) -> int:
    match = re.search("Ch [0-9]+", data)
    return int(match.group(0)[2:])


def __update_serie(cursor, short:str, episode_number:int) -> None:
    querry = cursor.execute("UPDATE urls SET episode_number = ? WHERE short = ? ", (episode_number, short))


def __make_serie_dict(short:str, 
                    url:str, 
                    episode_number:int, 
                    older_episode_number:int) -> dict :

    return {"short"                : short,
            "url"                  : url,
            "episode_number"       : episode_number,
            "older_episode_number" : older_episode_number 
            }


def get_new_episode(bdd_location:str) -> dict:
    """
    return only series with new episode
    """
    connection = core.modele.init_connection(bdd_location)
    if not connection:
        return None
    
    cursor   = connection.cursor()
    querry = cursor.execute("SELECT short, url, episode_number FROM urls")
    
    serie  = {}
    buffer = []

    for response in querry.fetchall():
        serie_informations         = __get_technical_div(response[1])
        number_of_episode_from_web = __isolate_episode_number(serie_informations)

        if number_of_episode_from_web > response[2]:
            buffer.append(__make_serie_dict(response[0], response[1], number_of_episode_from_web, response[2]))
    
            __update_serie(cursor, response[0], number_of_episode_from_web)
            connection.commit()
    
    serie["series"] = buffer
    connection.close()

    if len(serie["series"]) == 0:
        serie["series"] = [__make_serie_dict("Pas de nouveau épisode", "", "", "")]


    return serie
