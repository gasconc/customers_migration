from files import read_file
from mercadoPago import create_customer, tokenize, save_card, set_default_card
import json

if __name__ == "__main__":
    
    user={}

    user= json.loads(read_file(1,user))
    print (user)
    


    #Create Customer
    customer_id = create_customer(user)
    print (customer_id)

    #Tokenize card
    token = tokenize(user)
    print(token)

    #Save Card
    save_card(customer_id, token)

    #set default card
    


