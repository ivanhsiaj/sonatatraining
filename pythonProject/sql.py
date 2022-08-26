import pyodbc
server = 'HYDTRNG1\SQLEXPRESS'
database = 'training'
username = 'sa'
password = 'Jaishu12@'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
mycursor = cnxn.cursor()
res = mycursor.execute("select * from emp")
myrecs = res.fetchall();
print(myrecs)