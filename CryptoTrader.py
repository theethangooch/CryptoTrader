from dataclasses import dataclass
from coinbase.wallet.client import Client
import smtplib, ssl
import cbpro
import json
import time




public_client = cbpro.PublicClient()


with open('config.json') as config_file:
    data = json.load(config_file)
    
name_list = data['currencies']
lower_limit = data['lower_limit']
upper_limit = data['upper_limit']
key = data['api_key']
b64secret = data['secret_key']
passphrase = data['passphrase']
email = data['email']




@dataclass
class currency():

    name: str
    change: float
    same: float
    number: int
    open_var: int
    last_var: int

def get_balance(name):
    
    auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
    
    ok = name.split('-')
    final = ok[0]
    
    a = json.dumps(auth_client.get_accounts())
    b = json.loads(a)
    
    for x in b:
        if x['currency'] == final:
            return x['balance']
        
        
def buy(name):

    auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
    
    balance = get_balance("USD-USD")
    
    print(auth_client.buy(funds=balance, #USD
                order_type='market',
                product_id=name))
        
        
def sell(name):

    auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
    
    balance = get_balance(name)
    
    print(auth_client.sell(size=balance, #USD
                order_type='market',
                product_id=name))


def send_email(buy_sell, name):

    body = ""
    if buy_sell == 0:
        subject = "Bought " + name
    if buy_sell == 1:
        subject = "Sold " + name

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ethancrypto6879@gmail.com"  # Enter your address
    receiver_email = "ethancrypto6879@gmail.com"  # Enter receiver address
    password = "L23978eg"
    message = """\
    Subject: %s
    %s.""" %(subject,body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
       
    
has = 0

curr_list = []

num = 1
for x in name_list:
    curr_list.append(currency(x,0.0,99,num,None,None))
    num = num + 1



track = 0

while True:

    #update % change within past 24 hr
    if track != 0:
        time.sleep(30)
    for x in curr_list:

        a = json.dumps(public_client.get_product_24hr_stats(x.name))
        b = json.loads(a)
        if 'open' in b:
            c = b['open']
            x.open_var = 1
        else:
            x.open_var = 0
        if 'last' in b:
            d = b['last']
            x.last_var = 1
        else:
            x.last_var = 0
        if x.open_var == 1 and x.last_var == 1:
            x.change = ((float(d)-float(c))/float(c))*100

    #Print all stuff/buy and sell
    for x in curr_list:
        
        if x.open_var == 1 and x.last_var == 1:
            if x.change != 0.0 and x.change != x.same:
                print(x.name + ":\t " + str(x.change))
                x.same = x.change
                
            if x.change > upper_limit and int(has) == x.number:
                print("Sell: " + x.name)
                sell(x.name)
                send_email(1,x.name)
                has = 0

              
            if x.change < lower_limit and int(has) == 0:
                print("Buy: " + x.name)
                buy(x.name)
                send_email(0,x.name)
                has = x.number

            
    if track == 0:
        print("-------------------------------------------")
        track = track + 1
 
