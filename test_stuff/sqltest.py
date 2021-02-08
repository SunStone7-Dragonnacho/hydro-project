import sqlite3 

conn = sqlite3.connect('dat_col.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE data (
            datetime text,
            photoid text,
            is_pump_on text,
            is_light_on text
            )""")

'''
'''
#c.execute("INSERT INTO foods VALUES ('Pizza', 'Flatbread', 'Italy')")

c.execute("SELECT * FROM foods WHERE name='Pizza'")
print(c.fetchall())

conn.commit()

conn.close()
'''

# datetime, photoid, is_pump_on, is_light_on, 