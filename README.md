### MercadoPago Customers&Cards migration
Script for migration of Customers &amp; Cards to MercadoPago account

### The proccess:
![image](https://user-images.githubusercontent.com/25534296/79349647-148f1080-7efc-11ea-9eb7-b38cdf920edb.png)

### Getting started
1- Install the dependences: 
```
$pip3 install -r requirements.txt
```

2- You need to create a file named Data.xlsx with the Customers & Cards Data , format example is in the project.

![image](https://user-images.githubusercontent.com/25534296/79349811-4ef8ad80-7efc-11ea-8ea7-f2c29ffb4e3e.png)

3- Set your MercadoPago Credentials in the lines 5,6 over the file mercadoPago.py , your credentials are available in https://www.mercadopago.com/mco/account/credentials

4- Run the main file: 
```
$Python3 main.py
```

5- Review your logs.log file

## Topics:

- success rate: successfully users created over the total users

## Extra documentation:

- Youtube video explanation: available soon
