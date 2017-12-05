# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:51:50 2017

@author: dimitri.cabaud
"""

import pyodbc
import csv

[x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\dimitri.cabaud\Documents\171121_Basedonnée_agrégée_v5.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)
    

crsr.execute("SELECT * FROM table_transaction_finale_v5");

# OPEN CSV AND ITERATE THROUGH RESULTS
with open('Output.csv', 'w', newline='') as f:
    writer = csv.writer(f)    
    for row in crsr.fetchall() :
        writer.writerow(row)

crsr.close()
