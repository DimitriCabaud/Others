# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pypyodbc
import csv

# MS ACCESS DB CONNECTION
pypyodbc.lowercase = False
conn = pypyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
    r"Dbq=C:\Users\dimitri.cabaud\Documents\171121_Basedonnée_agrégée_v5.accdb;")

# OPEN CURSOR AND EXECUTE SQL
cur = conn.cursor()

cur.execute("SELECT * FROM table_transaction_finale_v5");

# OPEN CSV AND ITERATE THROUGH RESULTS
with open('Output.csv', 'w', newline='') as f:
    writer = csv.writer(f)    
    for row in cur.fetchall() :
        writer.writerow(row)

cur.close()
conn.close()