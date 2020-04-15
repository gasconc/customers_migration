import xlrd
import xlwt
import pymysql.cursors
import json


def read_file(row,user):
    loc = ("Data.xlsx") 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    user ={
        "metadata":{
            "id" : str(int(sheet.cell_value(row , 0))),
            "issuer":  str(sheet.cell_value(row , 7)),
            "payment_method":  str(sheet.cell_value(row , 8))
        },
        "identification" : {
            "type": str(sheet.cell_value(row , 1)), 
            "number":str(sheet.cell_value(row , 2)),
        },
        "first_name" : str(sheet.cell_value(row , 3)),
        "last_name" : str(sheet.cell_value(row , 4)) + ' '+ str(sheet.cell_value(row , 5)),
        "email":str(sheet.cell_value(row , 6)),

        "card_number" : str(sheet.cell_value(row , 9)),
        "expiration_month": str(sheet.cell_value(row , 10)).split('-')[1], 
        "expiration_year": str(sheet.cell_value(row , 10)).split('-')[0]
        }
    return json.dumps(user)
