import json
import requests

#Global Variables
PK=''
AT=''
headers = {"Content-Type": "application/json"}


def tokenize(user):
    global PK,AT,headers
    body= { 
        "card_number": user['card_number'],
        "expiration_month":user['expiration_month'], 
        "expiration_year": user['expiration_year'], 
        "cardholder": { 
            "name": user['first_name'] + ' ' + user['last_name'],
            "identification": user['identification']
        }
    }

    result = requests.post('https://api.mercadopago.com/v1/card_tokens?public_key='+ PK, headers=headers, data= json.dumps(body))
    return str(result.json()['id'])
    
def create_customer (user):
    global PK,AT,headers
    body={
        "email":user['email'],
        "first_name":user['first_name'],
        "last_name":user['last_name'],
        "identification":user['identification'],
        "metadata": user['metadata']
	
    }

   
    result = requests.post('https://api.mercadopago.com/v1/customers?access_token='+AT,headers=headers, data= json.dumps(body))
    return (result.json()['id'])
    

def save_card(customer_id, token): 
    global PK,AT,headers
    body={
        "token":token
    }
    result = requests.post('https://api.mercadopago.com/v1/customers/'+str(customer_id)+'cards?access_token='+AT,headers=headers, data= json.dumps(body))
    return  str(result.json())

def set_default_card(customer_id,card_id):
    global PK,AT,headers
    pass
 
