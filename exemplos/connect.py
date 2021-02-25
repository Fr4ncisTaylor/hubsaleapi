from HubSale import HubSale
from pprint  import pprint

client_id     = ""
client_secret = ""

hubsale       = HubSale(client_id, client_secret)
code, message = hubsale.connect()

if code:
	print("Success!!!")
else:
	print('Oops,', message)