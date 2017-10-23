import sqlite3
from AcademicTable import AcademicTable
conne = sqlite3.connect("Mil.db")
cursor = conne.cursor()
credit = []
creditAcademic = []
creditOfAcademic = []
listSum = []

def sum_credit():
    cursor.execute('''SELECT Credits FROM ACADEMIC''')
    for i in cursor:
        for j in i:
            credit.append(float(j))
    sumCredit = sum(credit)
    return sumCredit

def credit_of_academic():
    val = 1
    cursor.execute('''SELECT Credits,Academic regcord FROM ACADEMIC''')
    for i in cursor:
        creditAcademic.append(i)
    for u in creditAcademic:
        a = float(u[0])*float(u[1])
        listSum.append(a)
    print(listSum)
    sumListSum = sum(listSum)
    return sumListSum


def GPACal():
    Sumcredit = sum_credit()
    creditOfAca = credit_of_academic()
    Gpa = creditOfAca/Sumcredit
    print('%.2f' % Gpa)
print(GPACal())
