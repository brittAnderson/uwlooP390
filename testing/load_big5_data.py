import sqlite3 as s
import csv
import os

# Remove existing database to start fresh
if os.path.exists("big5.db"):
    os.remove("big5.db")

with open("./BIG5/BIG5/data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter='\t')
    rows = list(reader)

big5 = s.connect("big5.db")
cursor = big5.cursor()

cursor.execute("""
CREATE TABLE responses (
id INTEGER PRIMARY KEY AUTOINCREMENT,
race INTEGER,
age  INTEGER,
engnat INTEGER,
gender INTEGER,
hand INTEGER,
source TEXT,
country TEXT,
E1  INTEGER, 
E2  INTEGER,  
E3  INTEGER,  
E4  INTEGER,  
E5  INTEGER,  
E6  INTEGER,  
E7  INTEGER,  
E8  INTEGER,  
E9  INTEGER,  
E10 INTEGER,  
N1  INTEGER,  
N2  INTEGER,  
N3  INTEGER,  
N4  INTEGER,  
N5  INTEGER,  
N6  INTEGER,  
N7  INTEGER,  
N8  INTEGER,  
N9  INTEGER,  
N10 INTEGER,  
A1  INTEGER,  
A2  INTEGER,  
A3  INTEGER,  
A4  INTEGER,  
A5  INTEGER,  
A6  INTEGER,  
A7  INTEGER,  
A8  INTEGER,  
A9  INTEGER,  
A10 INTEGER,  
C1  INTEGER,  
C2  INTEGER,  
C3  INTEGER,  
C4  INTEGER,  
C5  INTEGER,  
C6  INTEGER,  
C7  INTEGER,  
C8  INTEGER,  
C9  INTEGER,  
C10 INTEGER,  
O1  INTEGER,  
O2  INTEGER,  
O3  INTEGER,  
O4  INTEGER,  
O5  INTEGER,  
O6  INTEGER,  
O7  INTEGER,  
O8  INTEGER,  
O9  INTEGER,  
O10 INTEGER)
""")

big5.commit()

# Get column names from CSV (excluding 'id' since it's auto-increment)
colnames = [col for col in rows[0].keys()]

# Create proper SQL with column names and placeholders
colnames_str = ','.join(colnames)
valueentry = ','.join(['?'] * len(colnames))

# Convert dictionaries to tuples in the correct order
row_tuples = [tuple(row[col] for col in colnames) for row in rows]

cursor.executemany(f"""
INSERT INTO responses ({colnames_str}) VALUES ({valueentry})""", row_tuples)

big5.commit()
big5.close()

print(f"Successfully loaded {len(rows)} rows into big5.db")


