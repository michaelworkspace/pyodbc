import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=localhost;'
    'Database=pltfloor;'
    'Trusted_Connection=yes'
)

cursor = conn.cursor()

cursor.execute(
    'SELECT c.CustomerId, c.CustomerName FROM CUSTOMERS c')

for row in cursor:
    print(row)
