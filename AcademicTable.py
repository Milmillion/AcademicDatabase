import sqlite3
class AcademicTable:
    def __init__(self):
        self.id = None

    def term(self,row):
        print("Term = ",row[0])

    def subID(self,row):
        print("Subject ID = ",row[1])

    def subName(self,row):
        print("Name subject = ",row[2])

    def credit(self,row):
        print("Credits = ",row[3])

    def acaReg(self,row):
        print("Academic regcord = ",row[4])

    def alldata(self,row):
        for item in row:
            print(item)

conne = sqlite3.connect("Mil.db")
cursor = conne.cursor()

# cursor.execute(''' CREATE TABLE ACADEMIC (Term TEXT, Subject ID TEXT,
#                 Name subject TEXT, Credits TEXT, Academic regcord TEXT)''')

# cursor.execute("""insert into ACADEMIC values('1/2560', 'FRA221', 'DIGITAL ELECTRONIC', '3', '4')""")
# cursor.execute("""insert into ACADEMIC values('1/2560', 'FRA222', 'INDUSTRIAL SENSORSAND ACTUATORS', '3', '4')""")
# cursor.execute("""insert into ACADEMIC values('1/2560', 'FRA231', 'STATICS AND DYNAMICS', '3', '3.5')""")
# cursor.execute("""insert into ACADEMIC values('1/2560', 'FRA241', 'SOFTWARE DEVELOPMENT', '3', '3')""")
# cursor.execute("""insert into ACADEMIC values('1/2560', 'FRA261', 'ROBOTICSAND AUTOMATION ENGINEERING', '1', '3.5')""")
# cursor.execute("""insert into ACADEMIC values('1/2560', 'LNG102', 'TECHNICAL ENGLISH', '3', '3.5')""")
# cursor.execute("""insert into ACADEMIC values('1/2560', 'MTH201', 'MATHEMATICS III', '3', '2.5')""")
# conne.commit()
