import sqlite3
class AcademicTable:
    def __init__(self):
        self.id = None

    def subID(self,row):
        print("Subject ID = ",row[0])

    def subName(self,row):
        print("Name subject = ",row[1])

    def credit(self,row):
        print("Credits = ",row[2])

    def acaReg(self,row):
        print("Academic regcord = ",row[3])

    def alldata(self,row):
        for item in row:
            print(item)

conne = sqlite3.connect("59340500035.db")
cursor = conne.cursor()
print (acaReg())


# cursor.execute(''' CREATE TABLE "1/2559" (Subject ID TEXT,Name subject TEXT, Credits TEXT, Academic regcord TEXT)''')
# cursor.execute(''' CREATE TABLE "2/2559" (Subject ID TEXT,Name subject TEXT, Credits TEXT, Academic regcord TEXT)''')
# cursor.execute(''' CREATE TABLE PROFILE (Name Student TEXT,
#                 Dateofbirth TEXT, Brithplace TEXT, Nationality TEXT, Education TEXT,
#                 Disease TEXT, Relative TEXT, PhoneforEmergency TEXT, Phonestudent TEXT, Address TEXT, Email TEXT)''')
# cursor.execute('''CREATE TABLE ACTIVITY
#                     (Name Activity TEXT, Description TEXT,
#                      Photo TEXT, TYPE TEXT, Advisor TEXT, Date_Activity TEXT, File TEXT, Confirm NULL)''')

# cursor.execute("""insert into "1/2559" values('FRA141', 'COMPUTER PROGRAMMING', '3', '4')""")
# cursor.execute("""insert into "1/2559" values('FRA161', 'ROBOTICS EXPLORATION', '3', '3')""")
# cursor.execute("""insert into "1/2559" values('GEN101', 'PHYSICAL EDUCATION', '1', '3.5')""")
# cursor.execute("""insert into "1/2559" values('LNG101', 'GENERAL ENGLISH', '3', '3')""")
# cursor.execute("""insert into "1/2559" values('MTH101', 'MATHEMATICS I', '3', '4')""")
# cursor.execute("""insert into "1/2559" values('PHY103', 'GENERAL PHYSICS', '3', '3.5')""")
# cursor.execute("""insert into "1/2559" values('PHY191', 'GENERAL PHYSICS LABORATORY I', '1', '4')""")
#
# cursor.execute("""insert into "2/2559" values('FRA121', 'ELECTRONIC CIRCUITS', '3', '3.5')""")
# cursor.execute("""insert into "2/2559" values('FRA142', 'COMPUTER PROGRAMMING', '3', '4')""")
# cursor.execute("""insert into "2/2559" values('FRA162', 'ROBOTICS AND AUTOMATION', '1', '3.5')""")
# cursor.execute("""insert into "2/2559" values('FRA163', 'ROBOTICS MACHINE SHOP', '1', '3')""")
# cursor.execute("""insert into "2/2559" values('GEN111', 'MAN AND ETHICS OF LIVING', '3', '3.5')""")
# cursor.execute("""insert into "2/2559" values('GEN121', 'LEARNING AND PROBLEM SOLVING SKILLS', '3', '2.5')""")
# cursor.execute("""insert into "2/2559" values('MTH102', 'MATHEMATICS II', '3', '2')""")
#
# cursor.execute("""insert into PROFILE values('Panchalee', '29/05/40', 'thailand', 'thai',
# 'Bachelor', 'None', 'Mother', '099-7654321', '084-7654321',  'Bangkok', 'popperzz@gmail.com')""")
#
# cursor.execute("INSERT INTO ACTIVITY values('Panchalee', 'It is will be useful.', 'Popperzz.jpg','Digital', 'Prof.Pi', '15/12/60', 'file of the Digital','comfirm')")
#
# conne.commit()
