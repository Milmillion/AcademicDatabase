import sqlite3
from AcademicTable import AcademicTable
A = "1/2559"
B = 59340500017
conne = sqlite3.connect(str(B) + ".db")
cursor = conne.cursor()

def sum_credit():
    credit = []
    cursor.execute('''SELECT Credits FROM "{}"'''.format(A))
    for i in cursor:
        for j in i:
            credit.append(float(j))
    sumCredit = sum(credit)
    return sumCredit

def credit_of_academic():
    creditAcademic = []
    listSum = []
    cursor.execute('''SELECT Credits,Academic regcord FROM "{}"'''.format(A))
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
