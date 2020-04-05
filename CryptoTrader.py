from dataclasses import dataclass
from coinbase.wallet.client import Client
import cbpro
import json

public_client = cbpro.PublicClient()

#--------------------------------------------------------------------------------------------------------

name_list = ["BAT-USDC","LINK-USD","REP-USD","ATOM-USD","XTZ-USD","DASH-USD"]
lower_limit = -10
upper_limit = 10

key = ""
b64secret = ""
passphrase = ""

#--------------------------------------------------------------------------------------------------------

@dataclass
class currency():

    name: str
    curr_price: float
    start_price: float
    change: float
    same: float
    number: int

#Returns balance of 'name'
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
        

has = 0

curr_list = []

num = 1
for x in name_list:

    a = json.dumps(public_client.get_product_ticker(x))
    b = json.loads(a)
    c = b['price']
    curr_list.append(currency(x,c,None,0.0,99,num))
    num = num + 1


for x in curr_list:
    print(x.name + " Start: ")
    x.start_price = input()


print ("Who has? 0=none")
has = input()


while True:

    #update curr_price
    for x in curr_list:
        a = json.dumps(public_client.get_product_ticker(x.name))
        b = json.loads(a)
        if 'price' in b:
            x.curr_price = b['price']
        else:
            print("NO KEY")
    
    
    #update changes in price
    for x in curr_list:
        x.change = ((float(x.curr_price) - float(x.start_price)) / float(x.start_price))*100
    
    
 
    for x in curr_list:
        
        if x.change != 0.0 and x.change != x.same:
            print(x.name + ":\t " + str(x.change))
            x.same = x.change
            
        if x.change > upper_limit and int(has) == x.number:
            print("Sell: " + x.name)
            sell(x.name)
            has = 0
            x.change = 0.0
            x.start_price = x.curr_price
          
        if x.change < lower_limit and int(has) == 0:
            print("Buy: " + x.name)
            buy(x.name)
            has = x.number
            x.change = 0.0
            x.start_price = x.curr_price
            


            
    
    
    
