import sqlite3
from AcademicTable import AcademicTable
class InputData:
    def __init__(self):
        self.id = None
conne = sqlite3.connect("mil.db")
cursor = conne.cursor()

# cursor.execute("""insert into PROFILE values('1/2559', 'FRA221', 'Digital electronic', '3', 'A')""")
# conne.commit()


conne.row_factory = sqlite3.Row

cursor.execute("SELECT * FROM ACADEMIC")

Aca = AcademicTable()
roww = cursor.fetterm()
Aca.alldata(roww)
