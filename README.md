# CryptoTrader
Automatically trades cryptocurrency with a coinbase pro account.

# Install
`pip install cbpro`  
`pip install coinbase`  

# Config
### Edit these lines
`currencies = ["BAT-USDC","LINK-USD","REP-USD","ATOM-USD","XTZ-USD","DASH-USD"] `  
`lower_limit = -10  `  
`upper_limit = 10  `  
`api_key = ""  `  
`secret_key = ""  `  
`passphrase = ""  `    
`email = ""  `  
  
  ### currencies: 
  Enter currencies you would like to include.  
  ### lower_limit: 
  When % change drops below this, the program buys.
  ### upper_limit: 
  When % change is above this, the program sells.  
  ### api_key: 
  Your coinbase api key.  
  ### secret_key: 
  Your coinbase secret key.  
  ### passphrase: 
  Your coinbase passphrase.  
  ### email: 
  Enter your email for buy/sell notifications.  
