from matplotlib import pyplot as plt
import datetime
import pyodbc

#! Connection String
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=localhost;'
    'Database=pltfloor;'
    'Trusted_Connection=yes'
)

cursor = conn.cursor()

# ? Convert a String to a DateTime object
start_date_str = input('Start Date: ')
start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')

# ? Convert a String to a DateTime object
end_date_str = input('End Date: ')
end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')

# ? The result set for the query
cursor.execute(
    f"""
    SELECT TOP 10 
    sm4.Setups.BoardGrade
    , dbo.f_convert(SUM(sm4.Setups.LinealRan), 'nanometers', 'feet') AS 'TotalLinealRan' 
    FROM sm4.Setups 
    INNER JOIN sm4.SetupProduction ON sm4.Setups.SetupKey = sm4.SetupProduction.SetupKey 
    WHERE sm4.SetupProduction.StartTime >= ? AND sm4.SetupProduction.EndTime < DATEADD(d, 1, ?) 
    GROUP BY sm4.Setups.BoardGrade 
    ORDER BY TotalLinealRan DESC
    """, start_date, end_date  # ? <- parameters goes here
)

plt.style.use('fivethirtyeight')

board_grade = []
total_lineal_ran = []

for row in cursor:
    board_grade.append(row[0])
    total_lineal_ran.append(row[1])

board_grade.reverse()
total_lineal_ran.reverse()

plt.barh(board_grade, total_lineal_ran, label='Board Grades')

plt.legend()

plt.title('Top 10 Board Grades by Lineal')
plt.xlabel('Lineal Ran (ft)')

plt.tight_layout()
plt.show()
