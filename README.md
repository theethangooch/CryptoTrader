# CryptoTrader
Automatically trades cryptocurrency with a coinbase pro account.

# Install
`pip install cbpro`  
`pip install coinbase`  

# Setup
### Edit these lines
`name_list = ["BAT-USDC","LINK-USD","REP-USD","ATOM-USD","XTZ-USD","DASH-USD"] `  
`lower_limit = -10  `  
`upper_limit = 10  `  
`key = ""  `  
`b64secret = ""  `  
`passphrase = ""  `    
  
  ### name_list: 
  Enter currencies you would like to include.  
  ### lower_limit: 
  When % change drops below this, the program buys.
  ### upper_limit: 
  When % change is above this, the program sells.  
  ### key: 
  Your coinbase api key.  
  ### b64secret: 
  Your coinbase secret key.  
  ### passphrase: 
  Your coinbase passphrase.  
