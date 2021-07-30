import sqlite3

def init_connection(bdd_location:str) -> sqlite3.Connection:
    """Init a connection with the database
    Parameters:
    bdd_location (str)   : str path to database
    
    Returns:
    sqlite3.Connection: Success
    None: Failed
    """
    try:
        return sqlite3.connect(bdd_location)
        
    except Exception as e:
        print(e)
        return None


def init_bdd(bdd_location:str) -> None:
    """Init the urls table if not exist
    Parameters:
    bdd_location (str)   : str path to database
    
    Returns: 
    None 
    """
    query = """CREATE TABLE IF NOT EXISTS "urls"  (
            "id"	         INTEGER PRIMARY KEY,
            "short"          TEXT    NOT NULL UNIQUE,
	        "url"	         TEXT    NOT NULL UNIQUE,
            "episode_number" INTEGER NOT NULL DEFAULT 0)"""

    connection = init_connection(bdd_location)
    
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
