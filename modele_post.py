import requests
import sqlite3
import re

from bs4      import BeautifulSoup

import modele_core

def add_serie(bdd_location:str, url:str, short:str) -> bool:
    connection = modele_core.init_connection(bdd_location)
    
    if not connection:
        return False
    
    cursor   = connection.cursor()
    querry = """INSERT INTO urls (url, short) VALUES (?,?)"""
    
    try:
        cursor.execute(querry, (url, short))
    except Exception as e:
        print(e)
        return False

    connection.commit()
    connection.close()

    return True