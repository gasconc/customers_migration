from files import read_file
from mercadoPago import create_customer, tokenize, save_card, set_default_card
import json
import logging
import xlrd
import requests
import xlwt
from xlwt import Workbook
import pandas as pd

#logging definitions
LOG_FILENAME = 'logs.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

#Sheet creation
loc = ("Data.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

# Output file
wb = Workbook()  
sheet1 = wb.add_sheet('Sheet 1')

#Printing output definition
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
#initialization
bodytech_ids=[]
customer_ids=[]
card_ids=[]

if __name__ == "__main__":
    
   
    exito=0
    fail = []
    total_users= sheet.nrows - 1 
    for i in range(1,sheet.nrows):
        try: 
            output = []
            user={}

            #read user from file
            user= json.loads(read_file(i,user))
            print (bcolors.OKGREEN + 'USER: ' + str(user['metadata']['id']))
            output.append(user['metadata']['id'])
            print ("<<------------------------------>>")
            
            #Create Customer
            customer_id = create_customer(user)
            print (bcolors.OKGREEN + 'CUSTOMER ID: ' + customer_id)
            output.append(customer_id)
            print ("<<------------------------------>>")

            #Tokenize card
            token = tokenize( user)
            output.append(token)
            print(bcolors.OKGREEN + 'CARD TOKEN: ' +token)
            print ("<<------------------------------>>")

            #Save Card
            card_id = save_card(customer_id, token)
            output.append(card_id)
            print (bcolors.OKGREEN + 'CARD ID: '+ str(card_id))
            print ("<<------------------------------>>")

            #set default card
            default_card = set_default_card(customer_id,card_id)
            exito = exito +1
    
            print(bcolors.WARNING + '>> Progreso: ' + str(int((i / total_users)*100 ) )+'% >> Success rate:' + str(int((exito / i)*100 ))+ '%' )
            print ("<< //////////////////////////// >>")

            #logging 
            
            logging.info('Customer creado con éxito: ' +str(output) )
            customer_ids.append(output[1])
            bodytech_ids.append(output[0])
            card_ids.append(output[3])
           

        except requests.exceptions.HTTPError as err:
            #handling exceptions
            print(err)
            #print(bcolors.FAIL + ' Error en la creación del usuario ' +  ' ERROR: ' + str(e) + ' - columna: ' + str(i))
            #print(bcolors.WARNING + '>> Progreso ' + str(int((i / total_users) *100 ))+'% >> Success rate:' + str(int((exito / i)*100 ))+ '%')
            logging.error ('Customer ha fallado en su creación: ' +str(output) + ' ERROR: ' + str(err) + ' - columna: ' + str(i))
            fail.append(str(user['metadata']['id']))

    #logging final metrics
    wb.save('output.xls') 
    print(bcolors.WARNING + 'Proceso finalizado >> Success rate:' + str(int((exito / i)*100) )+ '%')
    logging.info('Proceso finalizado >> Success rate:' + str(int((exito / i)*100) )+ '%')
    logging.info('lista de usuarios creados con error:  ' + str(fail))

    #writing output file
    raw_data={'Bodytech id':bodytech_ids,'Customer id':customer_ids,'Card id':card_ids}
    df=pd.DataFrame(raw_data, columns=['Bodytech id', 'Customer id', 'Card id'])
    output_workbook = 'output.xlsx'
    df.to_excel(output_workbook, index=False)
