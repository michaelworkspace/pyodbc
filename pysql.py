import pyodbc

#! Connection String
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=localhost;'
    'Database=pltfloor;'
    'Trusted_Connection=yes'
)

cursor = conn.cursor()

# ? The result set for the query
cursor.execute(
    'SELECT c.CustomerId, c.CustomerName FROM CUSTOMERS c')

cust_id = []
customer_name = []

for row in cursor:
    cust_id.append(row[0])
    customer_name.append(row[1])

print(cust_id)
print(customer_name)
