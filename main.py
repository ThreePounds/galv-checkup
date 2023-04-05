# --- imports ---

import sqlite3
import os.path

# --- constants ---
DATABASEFILE = 'examfile.db'

# --- interface ---



# --- initialize database ---

if os.path.isfile(DATABASEFILE):
    pass
else:
    #setting up data base file
    con = sqlite3.connect(DATABASEFILE)
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE employee("
            "name," 
            "givenname,"
            "id," # Lfd-Nummer
            "archived," # 1 wenn archiviert
            "hidden," # 1 wenn versteckt
            "birthyear,"
        ")"
    )
    con.commit()
    con.close()
    
# --- main event loop ---
