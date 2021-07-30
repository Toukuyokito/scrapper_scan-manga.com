import core.modele 

def add_serie(bdd_location:str, url:str, short:str) -> bool:
    connection = core.modele .init_connection(bdd_location)
    
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

def get_all_short(bdd_location:str) -> list:
    """
    return only series with new episode
    """
    connection = core.modele.init_connection(bdd_location)
    if not connection:
        return None
    
    cursor   = connection.cursor()
    querry = cursor.execute("SELECT short FROM urls")
    
    list_series_short:list[str] = []
    
    for answer in querry.fetchall():
        list_series_short.append(answer[0])

    connection.close()
    return list_series_short


def del_serie(bdd_location:str, serie:tuple) -> bool:
    
    connection = core.modele.init_connection(bdd_location)
    if not connection:
        return False
    
    cursor   = connection.cursor()

    try:
        cursor.execute(f"DELETE FROM urls where short in ({'?,' * (len(serie) - 1)}?)" , serie)
        connection.commit()
    
    except Exception as e:
        print(e)
        return False

    connection.close()
    return True