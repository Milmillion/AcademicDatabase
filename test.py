import sqlite3
from AcademicTable import AcademicTable
#from InputData import InputData
conne = sqlite3.connect("59340500035.db")
# conne.row_factory = sqlite3.Row
cursor = conne.cursor()
cursor.execute("SELECT * FROM ACTIVITY")

Aca = AcademicTable()
roww = cursor.fetchall()
Aca.alldata(roww)
