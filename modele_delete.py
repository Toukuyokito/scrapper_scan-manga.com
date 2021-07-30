import sqlite3
import modele_core

    
def del_serie(bdd_location:str, serie:tuple) -> bool:
    
    connection = modele_core.init_connection(bdd_location)
    if not connection:
        return False
    
    cursor   = connection.cursor()

    try:
        querry = cursor.execute(f"DELETE FROM urls where short in ({'?,' * (len(serie) - 1)}?)" , serie)
        connection.commit()
    
    except Exception as e:
        print(e)
        return False

    connection.close()
    return True
