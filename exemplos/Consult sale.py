from HubSale import HubSale
from pprint  import pprint

client_id     = "" # Your client ID
client_secret = "" # Your client secret

hubsale       = HubSale(client_id, client_secret)
code, message = hubsale.connect()

buy_code = 999999999 # client buy code

if code:
	# To officially consult
	pprint(hubsale.get_sale_by_code(buy_code))
	## To consult as a test
	pprint(hubsale.get_sale_by_code(buy_code, test=True))
else:
	print("Oops,", message)
