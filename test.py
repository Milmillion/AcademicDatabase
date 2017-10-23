import sqlite3
from AcademicTable import AcademicTable
#from InputData import InputData
conne = sqlite3.connect("Mil.db")
# conne.row_factory = sqlite3.Row
cursor = conne.cursor()
cursor.execute("SELECT * FROM ACADEMIC")

Aca = AcademicTable()
roww = cursor.fetchall()
Aca.alldata(roww)
